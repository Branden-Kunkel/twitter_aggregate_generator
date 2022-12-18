import twitterag.user_follows as user_follows
import twitterag.tweet_lookup as tweet_lookup
import twitterag.tweet_timeline as tweet_timeline
import twitterag.user_profile as user_profile
import twitterag.config_tools as config_tools
import twitterag.exceptions.auth_except as AuthEX
from time import sleep
import re
import json
import requests
import os
import sys
import cmd



# Likes Shell using Python standard library 'CMD'
#   
#   All shell commands are class methods prefixed with 'do_'. Example - do_help(), or do_profile()
#   All class methods/attributes are private unless they are a shell command method. 
#   Private attribute '__conf' is the configuration class instance. The vast majority of variables derive from this class
#   'AuthEX' is the shorthand for author defined exceptions imported from 'twitterag.exceptions' sub package
#   Besides 'do_profile', the class method 'retrieve_info()' is the aggregating method for this class. To see the flow of data and/or parameters, then start here
#



class likes(cmd.Cmd):

    """handles likes via tweet"""


    prompt = "MODULE@INFO-likes: "
    __conf = config_tools.ctools()
    __page_count = 0


    def do_liked(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:

            read_from_file_bool = self.__conf.likes_params["read_from_file?"]
            pagination_bool = self.__conf.likes_params["pagination"]["paginate?"]
            pagination_page_count = self.__conf.likes_params["pagination"]["page_count"]
            user_id_string = self.__conf.likes_params["user_id"]
            io_liked_readfile = self.__conf.file_IO["in"]["likes"]["user_id_list"]

            if read_from_file_bool == True:
                with open(io_liked_readfile, mode='r') as readfile:
                    for line in readfile:
                        if self.__input_file_check(line):
                            request = self.__retrieve_info(self.__url_build(user_id=line.strip(), url_type="liked"), self.__bearer_oauth_liked, self.__param_engine("liked"))
                            self.__dump_info(request, "liked")
                            self.__page_count = self.__page_count + 1
                            if pagination_bool == True:
                                while self.__page_count <= pagination_page_count:
                                    self.__conf.likes_params["liked_request_params"]["pagination_token"] = request["meta"]["next_token"]
                                    next_request = self.__retrieve_info(self.__url_build(user_id=line.strip(), url_type="liked"), oauth_type=self.__bearer_oauth_liked, params_type=self.__param_engine("liked"))
                                    request = next_request
                                    self.__dump_info(request, "liked")
                                    self.__page_count = self.__page_count + 1
                                self.__page_count = 0
                                return
                            elif pagination_bool == False:
                                self.__page_count = 0
                                return
                            else:
                                raise AuthEX.ParamTypeError(pagination_bool)
                        else:
                            print("\nNo data. Skipping line.\n")
                            pass
            elif read_from_file_bool == False:
                request = self.__retrieve_info(self.__url_build(user_id=user_id_string, url_type="liked"), self.__bearer_oauth_liked, self.__param_engine("liked"))
                self.__dump_info(request, "liked")
                self.__page_count = self.__page_count + 1
                if pagination_bool == True:
                    while self.__page_count <= pagination_page_count:
                        self.__conf.likes_params["liked_request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(user_id=user_id_string, url_type="liked"), oauth_type=self.__bearer_oauth_liked, params_type=self.__param_engine("liked"))
                        request = next_request
                        self.__dump_info(request, "liked")
                        self.__page_count = self.__page_count + 1
                    self.__page_count = 0
                    return
                elif pagination_bool == False:
                    self.__page_count = 0
                    return
                else:
                    raise AuthEX.ParamTypeError(pagination_bool)
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
            if "next_token" in key_error.args:
                pass
            else:
                print("\nConfig File Error: Bad key found in config file.\n")
                return

        except AuthEX.ParamTypeError as err:
            print("\nConfig File Error: Invalid parameter: " + str(err) + ".\n")
            return

        

    def do_liking(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:

            read_from_file_bool = self.__conf.likes_params["read_from_file?"]
            pagination_bool = self.__conf.likes_params["pagination"]["paginate?"]
            pagination_page_count = self.__conf.likes_params["pagination"]["page_count"]
            tweet_id_string = self.__conf.likes_params["tweet_id"]
            io_liking_readfile = self.__conf.file_IO["in"]["likes"]["tweet_id_list"] 

            if read_from_file_bool == True:
                with open(io_liking_readfile, mode='r') as readfile:
                    for line in readfile:
                        request = self.__retrieve_info(self.__url_build(tweet_id=line.strip(), url_type="liking"), self.__bearer_oauth_liking, self.__param_engine("liking"))
                        self.__dump_info(request, "liking")
                        self.__page_count = self.__page_count + 1
                        if pagination_bool == True:
                            while self.__page_count <= pagination_page_count:
                                self.__conf.likes_params["liking_request_params"]["pagination_token"] = request["meta"]["next_token"]
                                next_request = self.__retrieve_info(self.__url_build(tweet_id=line.strip(), url_type="liking"), oauth_type=self.__bearer_oauth_liking, params_type=self.__param_engine("liking"))
                                request = next_request
                                self.__dump_info(request, "liking")
                                self.__page_count = self.__page_count + 1
                            self.__page_count = 0
                            return
                        elif pagination_bool == False:
                            self.__page_count = 0
                            return
                        else:
                            raise AuthEX.ParamTypeError(pagination_bool)
            elif read_from_file_bool == False:
                request = self.__retrieve_info(self.__url_build(tweet_id=tweet_id_string, url_type="liking"), self.__bearer_oauth_liking, self.__param_engine("liking"))
                self.__dump_info(request, "liking")
                self.__page_count = self.__page_count + 1
                if pagination_bool == True:
                    while self.__page_count <= pagination_page_count:
                        self.__conf.likes_params["liking_request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(tweet_id=tweet_id_string, url_type="liking"), oauth_type=self.__bearer_oauth_liking, params_type=self.__param_engine("liked"))
                        request = next_request
                        self.__dump_info(request, "liking")
                        self.__page_count = self.__page_count + 1
                    self.__page_count = 0
                    return
                elif pagination_bool == False:
                    self.__page_count = 0
                    return
                else:
                    raise AuthEX.ParamTypeError(pagination_bool)
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
            print("\nConfig File Error: Invalid parameter: " + str(err) + "\n")
            return
        
    
    
    def do_list(self, arg):

        request_params = json.dumps(self.__conf.likes_params, indent=4, sort_keys=True)
        io_liking_readfile = self.__conf.file_IO["in"]["likes"]["tweet_id_list"]
        io_liked_readfile = self.__conf.file_IO["in"]["likes"]["user_id_list"]
        io_liking_writefile = self.__conf.file_IO["out"]["likes"]["liking"]
        io_liked_writefile = self.__conf.file_IO["out"]["likes"]["liked"]
        io_global = self.__conf.GLOBAL_FILE_PATH

        print("\n__Request__\n")
        print(str(request_params) + "\n")
        print("\n__Files__\n")
        print("    IN:")
        print("        " + io_liking_readfile)
        print("        " + io_liked_readfile)
        print("    OUT:")
        print("        " + io_liking_writefile)
        print("        " + io_liked_writefile)
        print("    GLOBAL:")
        print("        " + io_global)
        print("\n")

        return                 



    def do_set(self, arg):
        
        args_buff = str(arg)
        arg_list = args_buff.split()

        try:

            if arg_list[0] in ["request"]:
                if arg_list[1] in self.__conf.likes_params:
                    if arg_list[1] in ["liking_request_params"]:
                        if arg_list[2] in self.__conf.likes_params["liking_request_params"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.likes_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                    elif arg_list[1] in ["liked_request_params"]:
                        if arg_list[2] in self.__conf.likes_params["liked_request_params"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.likes_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                    elif arg_list[1] in ["pagination"]:
                        if arg_list[2] in self.__conf.likes_params["pagination"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.likes_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.likes_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                    else:
                        if arg_list[2] in ["true", "false", "none"]:
                            if arg_list[2] == "true":
                                self.__conf.likes_params[arg_list[1]] = True
                            elif arg_list[2] == "false":
                                self.__conf.likes_params[arg_list[1]] = False
                            else:
                                self.__conf.likes_params[arg_list[1]] = None
                        else:
                            self.__conf.likes_params[arg_list[1]] = arg_list[2]
                else:
                    raise AuthEX.ShellArgError(arg_list[1])
            elif arg_list[0] in ["files"]:
                if arg_list[1] in ["global"]:
                    self.__conf.GLOBAL_FILE_PATH = arg_list[2]
                elif arg_list[1] in self.__conf.file_IO:
                    if arg_list[1] in ["out"]:
                        if arg_list[2] in self.__conf.file_IO[arg_list[1]]["likes"]:
                            self.__conf.file_IO[arg_list[1]]["likes"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3]
                        else:
                                raise AuthEX.ShellArgError(arg_list[2])
                    else:
                        if arg_list[2] in self.__conf.file_IO["in"]["likes"]:
                            self.__conf.file_IO["in"]["likes"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3] 
                        else:
                            raise AuthEX.ShellArgError(arg_list[2])
                else:
                    raise AuthEX.ShellArgError(arg_list[1])
            else:
                raise AuthEX.ShellArgError(arg_list[0])
        
            self.do_list(arg=None)

        except IndexError as inx_err:
            print("\nNot enough arguments, or too many for this functionality. Use \'help\' or \'?\' for usage.\n")
            return

        except KeyError as key_error:
            print("\nError: Bad key in " + str(key_error.args))
            print("TIP: Config file corruption is possible with this error, but usually is due to a typo in args.\n")
            return

        except TypeError as t_err:
            print("\nError: Found \'None\' in: " + str(t_err.args) + ".\n")
            return

        except AuthEX.ShellArgError as err:
            print("\nError: Invalid shell argument specified: " + str(err) + ".\n")
            return



    def do_help(self, arg):
        commands_list = [   
                                    "liking = run the module with current parameters, returning which user have liked a target tweet id",
                                    "liked = run the module with current parameters, returning which tweets a target user id has liked",
                                    "set [arg]* = where arg is either \'files\' or \'params\', following args are keys in a dictionary structure, and last arg is the value to be set.",
                                    "list [arg] = where arg is \'params\', \'commands\' or omitted completely."
                                    "help = print a detailed help page for this module.",
                                    "exit = terminate the entire program instance.",
                                    "main = direct to the main console.",
                                    "user = direct to the tweet user profile console.",
                                    "timeline = direct to the tweet timeline console.",
                                    "follows = direct to the follows console.",
                                    "lookup = direct to the tweet lookup console."
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
        print("Terminating TAG...")
        sleep(2)
        sys.exit()



    def do_timeline(self, arg):
        tweet_timeline_console = tweet_timeline.tweet_timeline()
        tweet_timeline_console.cmdloop()



    def do_tweet(self, arg):
        tweet_lookup_console = tweet_lookup.tweet_lookup()
        tweet_lookup_console.cmdloop()



    def do_follows(self, arg):
        user_follows_console = user_follows.follows()
        user_follows_console.cmdloop()



    def do_user(self, arg):
        user_profile_console = user_profile.user_profile()
        user_profile_console.cmdloop()



    def __param_engine(self, param_type):

        params =    {

                    }

        liking_table = self.__conf.likes_params["liking_request_params"]
        liked_table = self.__conf.likes_params["liked_request_params"]

        if param_type == "liking":
            for key in liking_table:
                if liking_table[key] == None:
                    pass
                else:
                    params.update({key : liking_table[key]})
        elif param_type == "liked":
            for key in liked_table:
                if liked_table[key] == None:
                    pass
                else:
                    params.update({key : liked_table[key]})
        return params



    def __url_build(self, tweet_id="", user_id="", url_type=""): 

        if url_type == "liking":
            url = "https://api.twitter.com/2/tweets/{}/liking_users".format(tweet_id)
        elif url_type == "liked":
            url = "https://api.twitter.com/2/users/{}/liked_tweets".format(user_id)
            
        return url



    def __bearer_oauth_liking(self, r):  

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2LikingUsersPython"  
        
        return r

    def __bearer_oauth_liked(self, r):  

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2LikedTweetsPython"  
        
        return r


    def __retrieve_info(self, url, oauth_type, params_type): 
        
        request = requests.get(url, auth=oauth_type, params=params_type)

        info_out = request.json()

        if request.status_code != 200:
            
            print("Error(s): ")
            print(request.status_code)
            print(request.content)
            return
            
        elif request.status_code == 200:
            
            if self.__conf.genopts["verbose?"]:
                print("@" + url)
                print("Response successful!")

            return info_out



    def __dump_info(self, json_object, type):

        prettify = json.dumps(json_object, indent=4, sort_keys=True)

        if type == "liking":
            with open(self.__conf.file_IO["out"]["likes"]["liking"], mode='a') as writefile:
                json.dump(json_object, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")
        elif type == "liked":
            with open(self.__conf.file_IO["out"]["likes"]["liked"], mode='a') as writefile:
                json.dump(json_object, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")

        return


    def __dump_info(self, json_obj, type):

        try:

            prettify = json.dumps(json_obj, indent=4, sort_keys=True)

            writefile_path = ""


            if type == "liking":

                writefile_path = self.__conf.file_IO["out"]["likes"]["liking"]

            elif type == "liked":

                writefile_path = self.__conf.file_IO["out"]["likes"]["liked"]

            file_extension = os.path.splitext(writefile_path)[1]

            if os.path.isfile(writefile_path):
                pass
            else:
                raise FileNotFoundError

            if file_extension in [".json"]:
                with open(writefile_path, mode='a') as writefile:
                    json.dump(json_obj, writefile, indent=4, sort_keys=True)
                    if self.__conf.genopts["verbose?"]:
                        print(prettify)
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
