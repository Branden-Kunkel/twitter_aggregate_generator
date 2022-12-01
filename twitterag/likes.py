import twitterag.user_follows as user_follows
import twitterag.tweet_lookup as tweet_lookup
import twitterag.tweet_timeline as tweet_timeline
import twitterag.user_profile as user_profile
import twitterag.config_tools as config_tools
import json
from time import sleep
import requests
import os
import sys
import cmd
import errno

class likes(cmd.Cmd):

    """handles likes via tweet"""


    prompt = "MODULE@INFO-likes: "
    __conf = config_tools.ctools()
    __page_count = 0


    def do_liked(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        user_id = self.__conf.likes_params["user_id"]

        try:
            if self.__conf.likes_params["read_from_file?"]:
                with open(self.__conf.file_IO["in"]["likes"]["user_id_list"], mode='r') as readfile:
                    for line in readfile:
                        request = self.__retrieve_info(self.__url_build(user_id=line.strip(), url_type="liked"), self.__bearer_oauth_liked, self.__param_engine("liked"))
                        self.__dump_info(request, "liked")
                        self.__page_count = self.__page_count + 1
                        if self.__conf.likes_params["pagination"]["paginate?"]:
                            while self.__page_count <= self.__conf.likes_params["pagination"]["page_count"]:
                                self.__conf.likes_params["liked_request_params"]["pagination_token"] = request["meta"]["next_token"]
                                next_request = self.__retrieve_info(self.__url_build(user_id=line.strip(), url_type="liked"), oauth_type=self.__bearer_oauth_liked, params_type=self.__param_engine("liked"))
                                request = next_request
                                self.__dump_info(request, type="liked")
                                self.__page_count = self.__page_count + 1
                self.__page_count = 0
            else:
                request = self.__retrieve_info(self.__url_build(user_id=user_id, url_type="liked"), self.__bearer_oauth_liked, self.__param_engine("liked"))
                self.__dump_info(request, "liked")
                self.__page_count = self.__page_count + 1
                if self.__conf.likes_params["pagination"]["paginate?"]:
                    while self.__page_count <= self.__conf.likes_params["pagination"]["page_count"]:
                        self.__conf.likes_params["liked_request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(user_id=user_id, url_type="liked"), oauth_type=self.__bearer_oauth_liked, params_type=self.__param_engine("liked"))
                        request = next_request
                        self.__dump_info(request, type="liked")
                        self.__page_count = self.__page_count + 1
                self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: Read file not found")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")

        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")
            return 
            
        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")
            return 

        except KeyError as key_error:
            if "next_token" in key_error.args:
                pass
            else:    
                print("Config File Error: Bad key in " + str(key_error.args))
                return

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))
            print("Error: Found \'None\' in a required parameter ")
            return
        

    def do_liking(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        tweet_id = self.__conf.likes_params["tweet_id"]

        try:
            if self.__conf.likes_params["read_from_file?"]:
                with open(self.__conf.file_IO["in"]["likes"]["tweet_id_list"], mode='r') as readfile:
                    for line in readfile:
                        request = self.__retrieve_info(self.__url_build(tweet_id=line.strip(), url_type="liking"), self.__bearer_oauth_liking, self.__param_engine("liking"))
                        self.__dump_info(request, "liking")
                        self.__page_count = self.__page_count + 1
                        if self.__conf.likes_params["pagination"]["paginate?"]:
                            while self.__page_count <= self.__conf.likes_params["pagination"]["page_count"]:
                                self.__conf.likes_params["liking_request_params"]["pagination_token"] = request["meta"]["next_token"]
                                next_request = self.__retrieve_info(self.__url_build(tweet_id=line.strip(), url_type="liking"), oauth_type=self.__bearer_oauth_liking, params_type=self.__param_engine("liked"))
                                request = next_request
                                self.__dump_info(request, type="liking")
                                self.__page_count = self.__page_count + 1
                self.__page_count = 0
            else:
                request = self.__retrieve_info(self.__url_build(tweet_id=tweet_id, url_type="liking"), self.__bearer_oauth_liking, self.__param_engine("liked"))
                self.__dump_info(request, "liking")
                self.__page_count = self.__page_count + 1
                if self.__conf.likes_params["pagination"]["paginate?"]:
                    while self.__page_count <= self.__conf.likes_params["pagination"]["page_count"]:
                        self.__conf.likes_params["liking_request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(tweet_id=tweet_id, url_type="liking"), oauth_type=self.__bearer_oauth_liking, params_type=self.__param_engine("liked"))
                        request = next_request
                        self.__dump_info(request, type="liking")
                        self.__page_count = self.__page_count + 1
                self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: Read file not found")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")

        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")
        
        except KeyError as key_error:
            if "next_token" in key_error.args:
                pass
            else:
                print("Config File Error: Bad key in " + str(key_error.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))
        
    
    
    def do_list(self, arg):

        commands_list = [   
                            "liking = run the module in liking mode. No arguments.",
                            "liked = run the module in liked mode. No arguments."
                            "set [arg]* = where arg is either \'files\' or \'params\', following args are keys in a dictionary structure, and last arg is the value to be set.",
                            "list [arg] = where arg is \'params\', \'commands\' or omitted completely."
                            "help = print a detailed help page for this module.",
                            "exit = terminate the entire program instance.",
                            "main = direct to the main console.",
                            "timeline = direct to the tweet timeline console.",
                            "tweet = direct to the tweet lookup console.",
                            "follows = direct to the follows console.",
                            "user = direct to the user profile console."
                        ]

        if arg in ["params"]:
            print("\n__Configurations__")
            param_list = self.__conf.likes_params
            print("\n   Request:")
            for value in param_list:
                print("      " + str(value) + " = " + str(param_list[value]))
            files = self.__conf.file_IO
            print("\n   Files:")
            print("       out:")
            for value in files["out"]["likes"]:
                print("             " + str(value) + " = " + str(files["out"]["likes"][value]))
            print("       in:")
            for value in files["in"]["likes"]:
                print("             " + str(value) + " = " + str(files["in"]["likes"][value]))
            print("\n   GLOBAL FILE PATH:")
            print("         " + str(self.__conf.GLOBAL_FILE_PATH))
            print("\n")
        elif arg in ["commands"]:
            print("\n__Commands__")
            for value in commands_list:
                print("   " + value)
        else:
            print("\n__Configurations__")
            param_list = self.__conf.likes_params
            print("\n   Request:")
            for value in param_list:
                print("      " + str(value) + " = " + str(param_list[value]))
            files = self.__conf.file_IO
            print("\n   Files:")
            print("       out:")
            for value in files["out"]["likes"]:
                print("             " + str(value) + " = " + str(files["out"]["likes"][value]))
            print("       in:")
            for value in files["in"]["likes"]:
                print("             " + str(value) + " = " + str(files["in"]["likes"][value]))
            print("\nGLOBAL FILE PATH:")
            print("         " + str(self.__conf.GLOBAL_FILE_PATH))
            print("__Commands__\n")
            for value in commands_list:
                print("   " + value)
            print("\n")            



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
                            print("Invalid argument in: " + arg_list[2])
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
                            print("Invalid argument in: " + arg_list[2])
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
                            print("Invalid argument in: " + arg_list[2])
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
                    print("Invalid argument in: " + arg_list[1])
            elif arg_list[0] in ["files"]:
                if arg_list[1] in ["global"]:
                    self.__conf.GLOBAL_FILE_PATH = arg_list[2]
                elif arg_list[1] in self.__conf.file_IO:
                    if arg_list[1] in ["out"]:
                        if arg_list[2] in self.__conf.file_IO[arg_list[1]]["likes"]:
                            self.__conf.file_IO[arg_list[1]]["likes"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3]
                        else:
                                print("Invalid argument in: " + arg_list[2])
                    else:
                        if arg_list[2] in self.__conf.file_IO["in"]["likes"]:
                            self.__conf.file_IO["in"]["likes"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3] 
                        else:
                            print("Invalid argument in: " + arg_list[2])
                else:
                    print("Invalid argument in:" + arg_list[1])
            else:
                print("Invalid option in: " + arg_list[0])
        
            self.do_list(arg="params")

        except IndexError as inx_err:
            print("Not enough arguments, or too many for this functionality. Use \'list commands\'  for basic description or 'help' for detailed instructions.")
        
        except KeyError as key_error:
            print("Error: Bad key in " + str(key_error.args))
            print("TIP: Config file corruption is possible with this error, but usually is due to a typo in args")

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))



    def do_help(self, arg):
        self.do_list(arg="commands")
        print("\nFor in depth usage and information, see README.md in the source repo\n")
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



    def do_main(self, arg):
        os.system("python3 infoCLI.py")



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



    def __dump_info(self, json_object, type=""):

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
