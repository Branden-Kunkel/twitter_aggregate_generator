import twitterag.user_follows as user_follows
import twitterag.tweet_lookup as tweet_lookup
import twitterag.tweet_timeline as tweet_timeline
import twitterag.likes as likes
import twitterag.config_tools as config_tools
import twitterag.exceptions.auth_except as AuthEX
import json
import requests
import os
import sys
import cmd 
import cmd 
from time import sleep



# User Profile Shell using Python standard library 'CMD'
#   
#   All shell commands are class methods prefixed with 'do_'. Example - do_help(), or do_profile()
#   All class methods/attributes are private unless they are a shell command method. 
#   Private attribute '__conf' is the configuration class instance. The vast majority of variables derive from this class
#   'AuthEX' is the shorthand for author defined exceptions imported from 'twitterag.exceptions' sub package
#   Besides 'do_profile', the class method 'retrieve_info()' is the aggregating method for this class. To see the flow of data and/or parameters, then start here
#
 

 
class user_profile(cmd.Cmd):

    """handle requests for user profiles"""


    prompt = "MODULE@INFO-user: "

    __conf = config_tools.ctools()


    def do_profile(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:

            read_from_file_bool = self.__conf.user_profile_params["read_from_file?"]
            search_by_username_bool = self.__conf.user_profile_params["search_by_username?"]
            io_usernames_readfile = self.__conf.file_IO["in"]["user_profile"]["username_list"]
            io_userid_readfile = self.__conf.file_IO["in"]["user_profile"]["user_id_list"]
            usernames_string = self.__conf.user_profile_params["usernames"]
            user_id_string = self.__conf.user_profile_params["user_id"]

            shell_args_arg_buffer = str(arg)
            shell_args = shell_args_arg_buffer.split()

            if read_from_file_bool == True:
                if search_by_username_bool == True:
                    with open(io_usernames_readfile, mode='r') as readfile:
                        for line in readfile:
                            request = self.__retrieve_info(self.__url_build(usernames=line.strip()))
                            self.__dump_info(request)
                    return
                elif search_by_username_bool == False:
                    with open(io_userid_readfile, mode='r') as readfile:
                        for line in readfile:
                            request = self.__retrieve_info(self.__url_build(user_id=line.strip()))
                            self.__dump_info(request)
                    return
                else:
                    raise AuthEX.ParamTypeError
            elif read_from_file_bool == False:
                if search_by_username_bool == True:
                    request = self.__retrieve_info(self.__url_build(usernames_string))
                    self.__dump_info(request)
                    return
                elif search_by_username_bool == False:
                    request = self.__retrieve_info(self.__url_build(user_id=user_id_string))
                    self.__dump_info(request)
                    return
                else:
                    raise AuthEX.ParamTypeError
            else:
                raise AuthEX.ParamTypeError


        except FileNotFoundError:
            print("\nError: Readfile not found.\n")
            return

        except IsADirectoryError as dir_err:
            if dir_err.errno == 21:
                print("\nError: Readfile not found, only a directory. file_IO path is probably empty.\n")
            return

        except KeyError as key_error:
            print("\nConfig File Error: Bad key found in config file.\n")
            return

        except TypeError as t_err:
            print("\nError: Found \'None\' in: " + str(t_err.args) + "\n")

        except AuthEX.ParamTypeError:
            print("\nConfig File Error: Invalid or unexpected parameter found in config file.\n")
            return


    
    def do_list(self, arg):

        request_params = json.dumps(self.__conf.user_profile_params, indent=4, sort_keys=True)
        io_usernames_readfile = self.__conf.file_IO["in"]["user_profile"]["username_list"]
        io_user_id_readfile = self.__conf.file_IO["in"]["user_profile"]["user_id_list"]
        io_writefile = self.__conf.file_IO["out"]["user_profile"]["user_profiles"]
        io_global = self.__conf.GLOBAL_FILE_PATH

        print("\n__Request__\n")
        print(str(request_params) + "\n")
        print("\n__Files__\n")
        print("    IN:")
        print("        " + io_usernames_readfile)
        print("        " + io_user_id_readfile)
        print("    OUT:")
        print("        " + io_writefile)
        print("    GLOBAL")
        print("        " + io_global)
        print("\n")

        return
            


    def do_set(self, arg):
        
        args_buff = str(arg)
        arg_list = args_buff.split()

        try:

            if arg_list[0] in ["request"]:
                if arg_list[1] in self.__conf.user_profile_params:
                    if arg_list[1] in ["request_params"]:
                        if arg_list[2] in self.__conf.user_profile_params["request_params"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.user_profile_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.user_profile_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.user_profile_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.user_profile_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            raise AuthEX.ShellArgError
                    else:
                        if arg_list[2] in ["true", "false", "none"]:
                            if arg_list[2] == "true":
                                self.__conf.user_profile_params[arg_list[1]] = True
                            elif arg_list[2] == "false":
                                self.__conf.user_profile_params[arg_list[1]] = False
                            else:
                                self.__conf.user_profile_params[arg_list[1]] = None
                        else:
                            self.__conf.user_profile_params[arg_list[1]] = arg_list[2]
                else:
                    raise AuthEX.ShellArgError

            elif arg_list[0] in ["files"]:
                if arg_list[1] in ["global"]:
                    self.__conf.GLOBAL_FILE_PATH = arg_list[2]
                elif arg_list[1] in self.__conf.file_IO:
                    if arg_list[1] in ["out"]:
                        if arg_list[2] in self.__conf.file_IO[arg_list[1]]["user_profile"]:
                            self.__conf.file_IO[arg_list[1]]["user_profile"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3]
                        else:
                                raise AuthEX.ShellArgError
                    else:
                        if arg_list[2] in self.__conf.file_IO["in"]["user_profile"]:
                            self.__conf.file_IO["in"]["user_profile"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3] 
                        else:
                            raise AuthEX.ShellArgError
                else:
                    raise AuthEX.ShellArgError
            else:
                raise AuthEX.ShellArgError
        
            self.do_list(arg=None)
        
        except KeyError as key_error:
            print("Error: Bad key in: " + str(key_error.args))
            print("TIP: Config file corruption is possible with this error, but usually is due to a typo in args")
            return

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))
            return

        except IndexError as inx_err:
            print("Error: Not enough arguments, or too many for this functionality. Use \'help\' or \'?\' for basic command usage")
            return

        except AuthEX.ShellArgError:
            print("Error: Invalid shell argument specified.")
            return
        
        return
  

        
    def do_help(self, arg):
        commands_list = [   
                            "profile = run the module with current parameters. No arguments.",
                            "set [arg]* = where arg is either \'files\' or \'params\', following args are keys in a dictionary structure, and last arg is the value to be set.",
                            "list [arg] = where arg is \'params\', \'commands\' or omitted completely."
                            "help = print a detailed help page for this module.",
                            "exit = terminate the entire program instance.",
                            "main = direct to the main console.",
                            "timeline = direct to the tweet timeline console.",
                            "tweet = direct to the tweet lookup console.",
                            "follows = direct to the follows console.",
                            "likes = direct to the likes console."
                        ]
        print("\n__Commands__\n")

        for value in commands_list:
            print("    " + value + "\n")

        return



    def default(self, line: str):
        print("Invalid input...")
        return



    def emptyline(self):
        return
        


    def do_clear(self, arg):
        os.system("clear")
        return



    def do_exit(self, arg):
        print("Terminating")
        sleep(2)
        sys.exit()



    def do_main(self, arg):
        os.system("python3 infoCLI.py")



    def do_timeline(self, arg):
        timeline_module = tweet_timeline.tweet_timeline()
        timeline_module.cmdloop()



    def do_tweet(self, arg):
        tweet_lookup_console = tweet_lookup.tweet_lookup()
        tweet_lookup_console.cmdloop()



    def do_follows(self, arg):
        user_follows_console = user_follows.follows()
        user_follows_console.cmdloop()



    def do_likes(self, arg):
        likes_console = likes.likes()
        likes_console.cmdloop()

 

    def __param_engine(self):

        params =    {}
        param_table = self.__conf.user_profile_params["request_params"]

        for key in param_table:
            if param_table[key] == None:
                pass
            else:
                params.update({key : param_table[key]})

        return params



    def __url_build(self, usernames="", user_id=""):

        search_by_user = self.__conf.user_profile_params["search_by_username?"]
        user_list = "usernames={}".format(usernames) 

        if search_by_user:
                url = "https://api.twitter.com/2/users/by?{}".format(user_list)
        else:
            url = "https://api.twitter.com/2/users/{}".format(user_id)
            
        return url



    def __bearer_oauth(self, r):  

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2UserLookupPython"  
        
        return r



    def __retrieve_info(self, url): 
        
        auth = self.__bearer_oauth
        params = self.__param_engine()

        request = requests.get(url, auth=auth, params=params)
        info_out = request.json()
        prettify = json.dumps(info_out, sort_keys=True, indent=4)

        if request.status_code != 200:
            print("Error(s): ")
            print(request.status_code)
            print(request.content)
            return
            
        elif request.status_code == 200:    
            if self.__conf.genopts["verbose?"]:
                print("\nrequest @ " + url + "\n")
                print(prettify + "\n")
                print("Response successful!\n")

            return info_out



    def __dump_info(self, json_object):

        with open(self.__conf.file_IO["out"]["user_profile"]["user_profiles"], mode='a') as writefile:
            json.dump(json_object, writefile, indent=4, sort_keys=True)
            
        return


        

