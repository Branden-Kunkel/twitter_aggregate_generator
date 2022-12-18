import twitterag.user_follows as user_follows
import twitterag.user_profile as user_profile
import twitterag.tweet_timeline as tweet_timeline
import twitterag.likes as likes
import twitterag.config_tools as config_tools
import twitterag.exceptions.auth_except as AuthEX
from time import sleep
import re
import json
import requests
import os
import sys
import cmd



# Tweet Lookup Shell using Python standard library 'CMD'
#   
#   All shell commands are class methods prefixed with 'do_'. Example - do_help(), or do_profile()
#   All class methods/attributes are private unless they are a shell command method. 
#   Private attribute '__conf' is the configuration class instance. The vast majority of variables derive from this class
#   'AuthEX' is the shorthand for author defined exceptions imported from 'twitterag.exceptions' sub package
#   Besides 'do_profile', the class method 'retrieve_info()' is the aggregating method for this class. To see the flow of data and/or parameters, then start here
#



class tweet_lookup(cmd.Cmd):
    
    """single tweet lookup"""


    prompt = "MODULE@INFO-tweet: "

    __conf = config_tools.ctools()


    def do_lookup(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:

            read_from_file_bool = self.__conf.tweet_lookup_params["read_from_file?"]
            io_tweet_id_readfile = self.__conf.file_IO["in"]["tweet_lookup"]["tweet_id_list"]
            tweet_id_string = self.__conf.tweet_lookup_params["tweet_id"]

            if read_from_file_bool == True:
                with open(io_tweet_id_readfile, mode='r') as readfile:
                    for line in readfile:
                        if self.__input_file_check(line):
                            self.__dump_info(self.__retrieve_info(self.__url_build(line.strip())))
                        else:
                            print("\nNo data. Skipping line.\n")
                            pass
                return
            elif read_from_file_bool == False:
                self.__dump_info(self.__retrieve_info(self.__url_build(tweet_id_string)))
                return
            else:
                raise AuthEX.ParamTypeError(read_from_file_bool)

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

        except AuthEX.ParamTypeError as err:
            print("\nConfig File Error: Invalid parameter: " + str(err) + ".\n")
            return


    def do_list(self, arg):

        request_params = json.dumps(self.__conf.tweet_lookup_params, indent=4, sort_keys=True)
        io_tweet_id_readfile = self.__conf.file_IO["in"]["tweet_lookup"]["tweet_id_list"]
        io_lookup_writefile = self.__conf.file_IO["out"]["tweet_lookup"]["tweets"]
        io_global = self.__conf.GLOBAL_FILE_PATH

        print("\n__Request__\n")
        print(str(request_params) + "\n")
        print("\n__Files__\n")
        print("    IN:")
        print("        " + io_tweet_id_readfile)
        print("    OUT:")
        print("        " + io_lookup_writefile)
        print("    GLOBAL:")
        print("        " + io_global)
        print("\n")

        return      



    def do_set(self, arg):

        args_buff = str(arg)
        arg_list = args_buff.split()

        try:

            if arg_list[0] in ["request"]:
                if arg_list[1] in self.__conf.tweet_lookup_params:
                    if arg_list[1] in ["request_params"]:
                        if arg_list[2] in self.__conf.tweet_lookup_params["request_params"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.tweet_lookup_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.tweet_lookup_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.tweet_lookup_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.tweet_lookup_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                    else:
                        if arg_list[2] in ["true", "false", "none"]:
                            if arg_list[2] == "true":
                                self.__conf.tweet_lookup_params[arg_list[1]] = True
                            elif arg_list[2] == "false":
                                self.__conf.tweet_lookup_params[arg_list[1]] = False
                            else:
                                self.__conf.tweet_lookup_params[arg_list[1]] = None
                        else:
                            self.__conf.tweet_lookup_params[arg_list[1]] = arg_list[2]
                else:
                    raise AuthEX.ShellArgError(arg_list[1])

            elif arg_list[0] in ["files"]:
                if arg_list[1] in ["global"]:
                    self.__conf.GLOBAL_FILE_PATH = arg_list[2]
                elif arg_list[1] in self.__conf.file_IO:
                    if arg_list[1] in ["out"]:
                        if arg_list[2] in self.__conf.file_IO[arg_list[1]]["tweet_lookup"]:
                            self.__conf.file_IO[arg_list[1]]["tweet_lookup"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3]
                        else:
                                raise AuthEX.ShellArgError(arg_list[2])
                    else:
                        if arg_list[2] in self.__conf.file_IO["in"]["tweet_lookup"]:
                            self.__conf.file_IO["in"]["tweet_lookup"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3] 
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                else:
                    raise AuthEX.ShellArgError(arg_list[1])
            else:
                raise AuthEX.ShellArgError(arg_list[0])
        
            self.do_list(arg=None)
        
        except KeyError as key_error:
            print("\nError: Bad key in " + str(key_error.args))
            print("TIP: Config file corruption is possible with this error, but usually is due to a typo in args\n")
            return

        except TypeError as t_err:
            print("\nError: Found \'None\' in: " + str(t_err.args) + ".\n")
            return

        except IndexError as inx_err:
            print("\nNot enough arguments, or too many for this functionality. Use \'help\' or \'?\' for usage.\n")
            return

        except AuthEX.ShellArgError as err:
            print("\nError: Invalid shell argument specified: " + str(err) + ".\n")
            return

        return



    def do_help(self, arg):
        commands_list = [   
                                    "lookup = run the module with current parameters. No arguments.",
                                    "set [arg]* = where arg is either \'files\' or \'params\', following args are keys in a dictionary structure, and last arg is the value to be set.",
                                    "list [arg] = where arg is \'params\', \'commands\' or omitted completely."
                                    "help = print a detailed help page for this module.",
                                    "exit = terminate the entire program instance.",
                                    "main = direct to the main console.",
                                    "user = direct to the tweet user profile console.",
                                    "timeline = direct to the tweet timeline console.",
                                    "follows = direct to the follows console.",
                                    "likes = direct to the likes console."
                                ]
        print("\n__Commands__\n")

        for value in commands_list:
            print("    " + value + "\n")

        return



    def default(self, line: str):
        print("Invalid input...")
        sleep(1)
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
    


    def do_timeline(self, arg):
        tweet_timeline_console = tweet_timeline.tweet_timeline()
        tweet_timeline_console.cmdloop()



    def do_follows(self, arg):
        user_follows_console = user_follows.follows()
        user_follows_console.cmdloop()



    def do_user(self, arg):
        user_profile_console = user_profile.user_profile()
        user_profile_console.cmdloop()



    def do_likes(self, arg):
        likes_console = likes.likes()
        likes_console.cmdloop()



    def __url_build(self, tweet_ids):

        id_list = "ids={}".format(tweet_ids)

        url = "https://api.twitter.com/2/tweets?{}".format(id_list)
            
        return url



    def __param_engine(self):

            params = {}
            param_table = self.__conf.tweet_lookup_params["request_params"]

            for key in param_table:
                if param_table[key] == None:
                    pass
                else:
                    params.update({key : param_table[key]})

            return params



    def __bearer_oauth(self, r):  

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2TweetLookupPython"  
        
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

        try:

            writefile_path = self.__conf.file_IO["out"]["tweet_lookup"]["tweets"]
            file_extension = os.path.splitext(writefile_path)[1]

            if os.path.isfile(writefile_path):
                pass
            else:
                raise FileNotFoundError

            if file_extension in [".json"]:
                with open(writefile_path, mode='a') as writefile:
                    json.dump(json_object, writefile, indent=4, sort_keys=True)
                return    
            else:
                raise AuthEX.OutputFileError

        except AuthEX.OutputFileError:
            print("\nError: Writefile is not of .json type.\n")
            return
        
        except FileNotFoundError:
            print("\nError: Writefile not found.\n")
            return

        except IsADirectoryError:
            print("\nError: Writefile not found, found directory instead.\n")
            return  



    def __input_file_check(self, readline):

        regex_string = "[^\n\r\t\0]"
        regex_pattern = re.compile(regex_string)

        match_boolean = re.search(regex_pattern, readline)

        if match_boolean:
            return True
        elif match_boolean in [False, None]:
            return False
            

