import twitterag.user_profile as user_profile
import twitterag.tweet_lookup as tweet_lookup
import twitterag.tweet_timeline as tweet_timeline
import twitterag.likes as likes
import twitterag.config_tools as config_tools
import json
from time import sleep
import requests
import os
import sys
import cmd
import errno

class follows(cmd.Cmd):
    """ retrieves user follows """


    prompt = "MODULE@INFO-follows: "
    __conf = config_tools.ctools()
    __page_count = 0
    

    def do_followers(self, arg):

        try:
            print("\nRunning {}\n".format(self.prompt))
            if self.__conf.user_follows_params["read_from_file?"]:
                with open(self.__conf.file_IO["in"]["user_follows"]["user_id_list"]) as readfile:
                    for line in readfile:
                        request = self.__retrieve_info(self.__url_build(line.strip(), "followers"), self.__bearer_oauth_followers)
                        self.__dump_info(request, "followers")
                        self.__page_count = self.__page_count + 1
                        if self.__conf.user_follows_params["pagination"]["paginate?"]:
                            while self.__page_count <= self.__conf.user_follows_params["pagination"]["page_count"]:
                                    self.__conf.user_follows_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                                    next_request = self.__retrieve_info(self.__url_build(user_id=line.split(), follows_type="followers"), self.__bearer_oauth_followers)
                                    request = next_request
                                    self.__dump_info(request, "followers")
                                    self.__page_count = self.__page_count + 1
                        elif self.__conf.user_follows_params["pagination"]["paginate?"] == False:
                            self.__page_count = 0
                            return
                        else:
                            print("Invalid param type in: request >> pagination >> paginate?: " + str(self.__conf.user_follows_params["pagination"]["paginate?"]))
                            print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                            return

            elif self.__conf.user_follows_params["read_from_file?"] == False:
                user_id = self.__conf.user_follows_params["user_id"]
                request = self.__retrieve_info(self.__url_build(user_id, follows_type="followers"), self.__bearer_oauth_followers)
                self.__dump_info(request, type="followers")
                self.__page_count = self.__page_count + 1
                if self.__conf.user_follows_params["pagination"]["paginate?"]:
                    while self.__page_count <= self.__conf.user_follows_params["pagination"]["page_count"]:
                        self.__conf.user_follows_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(user_id, follows_type="followers"), self.__bearer_oauth_followers)
                        request = next_request
                        self.__dump_info(request, type="followers")
                        self.__page_count = self.__page_count + 1
                elif self.__conf.user_follows_params["pagination"]["paginate?"] == False:
                    self.__page_count = 0
                    return
                else:
                    print("Invalid param type in: request >> pagination >> paginate?: " + str(self.__conf.user_follows_params["pagination"]["paginate?"]))
                    print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                    return
            else:
                print("Invalid param type in: request >> read_from_file?: " + str(self.__conf.user_follows_params["read_from_file?"]))
                print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                return

            self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: Read File not found")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.") 
            return

        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")

        except KeyError as key_error:
            return
            
        except KeyError as key_error:
            if "next_token" in key_error.args:
                pass
            else:    
                print("Config File Error: Bad key in  " + str(key_error.args))
                return
        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in a required parameter ")
            return


    def do_following(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:
            if self.__conf.user_follows_params["read_from_file?"]:
                with open(self.__conf.file_IO["in"]["user_follows"]["user_id_list"]) as readfile:
                    for line in readfile:
                        request = self.__retrieve_info(self.__url_build(line.strip(), follows_type="following"), self.__bearer_oauth_following)
                        self.__dump_info(request, type="following")
                        self.__page_count = self.__page_count + 1
                        if self.__conf.user_follows_params["pagination"]["paginate?"]:
                            while self.__page_count <= self.__conf.user_follows_params["pagination"]["page_count"]:
                                self.__conf.user_follows_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                                next_request = self.__retrieve_info(self.__url_build(user_id=line.strip(), follows_type="following"), self.__bearer_oauth_following)
                                request = next_request
                                self.__dump_info(request, type="following")
                                self.__page_count = self.__page_count + 1
                        elif self.__conf.user_follows_params["pagination"]["paginate?"] == False:
                            self.__page_count = 0
                            return
                        else:
                            print("Invalid param type in: request >> pagination >> paginate?: " + str(self.__conf.user_follows_params["pagination"]["paginate?"]))
                            print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                            return
            elif self.__conf.user_follows_params["read_from_file?"] == False:
                user_id = self.__conf.user_follows_params["user_id"]
                request = self.__retrieve_info(self.__url_build(user_id, follows_type="following"), self.__bearer_oauth_following)
                self.__dump_info(request, type="following")
                self.__page_count = self.__page_count + 1
                if self.__conf.user_follows_params["pagination"]["paginate?"]:
                    while self.__page_count <= self.__conf.user_follows_params["pagination"]["page_count"]:
                        self.__conf.user_follows_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_info(self.__url_build(user_id, follows_type="following"), self.__bearer_oauth_following)
                        request = next_request
                        self.__dump_info(request, type="following")
                        self.__page_count = self.__page_count + 1
                elif self.__conf.user_follows_params["pagination"]["paginate?"] == False:
                    self.__page_count = 0
                    return
                else:
                    print("Invalid param type in: request >> pagination >> paginate?: " + str(self.__conf.user_follows_params["pagination"]["paginate?"]))
                    print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                    return 
            else:
                print("Invalid param type in: request >> read_from_file?: " + str(self.__conf.user_follows_params["read_from_file?"]))
                print("**Parameter of type BOOL can ONLY be \'True\' OR \'False\'")
                return

            self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: Read File not found")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")
                return 

        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")

        except KeyError as key_error:
            if "next_token" in key_error.args:
                pass
            else:
                print("Config File Error: Bad key in " + str(key_error.args))
                return


    
    def do_list(self, arg):

        commands_list = [   
                            "followers = run the module in followers mode. No arguments",
                            "following = run the module in following mode. No arguments"
                            "set [arg]* = where arg is either \'files\' or \'params\', following args are keys in a dictionary structure, and last arg is the value to be set.",
                            "list [arg] = where arg is \'params\', \'commands\' or omitted completely."
                            "help = print a detailed help page for this module.",
                            "exit = terminate the entire program instance.",
                            "main = direct to the main console.",
                            "timeline = direct to the tweet timeline console.",
                            "tweet = direct to the tweet lookup console.",
                            "user = direct to the user profile console.",
                            "likes = direct to the likes console."
                        ]

        if arg in ["params"]:
            print("\n__Configurations__")
            param_list = self.__conf.user_follows_params
            print("\n   Request:")
            for value in param_list:
                print("      " + str(value) + " = " + str(param_list[value]))
            files = self.__conf.file_IO
            print("\n   Files:")
            print("       out:")
            for value in files["out"]["user_follows"]:
                print("             " + str(value) + " = " + str(files["out"]["user_follows"][value]))
            print("       in:")
            for value in files["in"]["user_follows"]:
                print("             " + str(value) + " = " + str(files["in"]["user_follows"][value]))
            print("\n   GLOBAL FILE PATH:")
            print("         " + str(self.__conf.GLOBAL_FILE_PATH))
            print("\n")
        elif arg in ["commands"]:
            print("\n__Commands__")
            for value in commands_list:
                print("   " + value)
        else:
            print("\n__Configurations__")
            param_list = self.__conf.user_follows_params
            print("\n   Request:")
            for value in param_list:
                print("      " + str(value) + " = " + str(param_list[value]))
            files = self.__conf.file_IO
            print("\n   Files:")
            print("       out:")
            for value in files["out"]["user_follows"]:
                print("             " + str(value) + " = " + str(files["out"]["user_follows"][value]))
            print("       in:")
            for value in files["in"]["user_follows"]:
                print("             " + str(value) + " = " + str(files["in"]["user_follows"][value]))
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
                if arg_list[1] in self.__conf.user_follows_params:
                    if arg_list[1] in ["request_params"]:
                        if arg_list[2] in self.__conf.user_follows_params["request_params"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            print("Invalid argument in: " + arg_list[2])
                    elif arg_list[1] in ["pagination"]:
                        if arg_list[2] in self.__conf.user_follows_params["pagination"]:
                            if arg_list[3] in ["true", "false", "none"]:
                                if arg_list[3] == "true":
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = True
                                elif arg_list[3] == "false":
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = False
                                else:
                                    self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = None
                            else:
                                self.__conf.user_follows_params[arg_list[1]][arg_list[2]] = arg_list[3]
                        else:
                            print("Invalid argument in: " + arg_list[2])
                    else:
                        if arg_list[2] in ["true", "false", "none"]:
                            if arg_list[2] == "true":
                                self.__conf.user_follows_params[arg_list[1]] = True
                            elif arg_list[2] == "false":
                                self.__conf.user_follows_params[arg_list[1]] = False
                            else:
                                self.__conf.user_follows_params[arg_list[1]] = None
                        else:
                            self.__conf.user_follows_params[arg_list[1]] = arg_list[2]
                else:
                    print("Invalid argument in: " + arg_list[1])

            elif arg_list[0] in ["files"]:
                if arg_list[1] in ["global"]:
                    self.__conf.GLOBAL_FILE_PATH = arg_list[2]
                elif arg_list[1] in self.__conf.file_IO:
                    if arg_list[1] in ["out"]:
                        if arg_list[2] in self.__conf.file_IO[arg_list[1]]["user_follows"]:
                            self.__conf.file_IO[arg_list[1]]["user_follows"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3]
                        else:
                                print("Invalid argument in: " + arg_list[2])
                    else:
                        if arg_list[2] in self.__conf.file_IO["in"]["user_follows"]:
                            self.__conf.file_IO["in"]["user_follows"][arg_list[2]] = self.__conf.GLOBAL_FILE_PATH + arg_list[3] 
                        else:
                            print("Invalid argument in: " + arg_list[2])
                else:
                    print("Invalid argument in:" + arg_list[1])
            else:
                print("Invalid option in: " + arg_list[0])
        
            self.do_list(arg="params")
        
        except KeyError as key_error:
            print("Error: Bad key in " + str(key_error.args))
            print("TIP: Config file corruption is possible with this error, but usually is due to a typo in args")

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))

        except IndexError as inx_err:
            print("Not enough arguments, or too many for this functionality. Use \'list commands\'  for basic description or 'help' for detailed instructions.")

        

    def do_help(self, arg):
        self.do_list(arg="commands")
        print("\nFor in depth usage and information, see README.md in the source repo\n")
        return



    def default(self, line: str) -> None:
        print("Invalid input...")
        sleep(1)
        return



    def do_emptyline(self):
        return
        


    def do_exit(self, arg):
        print("Terminating TAG...")
        sleep(2)
        sys.exit()



    def do_clear(self, arg):
        os.system("clear")
        return



    def do_main(self, arg):
        os.system("python3 infoCLI.py")


    
    def do_timeline(self, arg):
        tweet_timeline_console = tweet_timeline.tweet_timeline()
        tweet_timeline_console.cmdloop()



    def do_tweet(self, arg):
        tweet_lookup_console = tweet_lookup.tweet_lookup()
        tweet_lookup_console.cmdloop()



    def do_user(self, arg):
        user_profile_console = user_profile.user_profile()
        user_profile_console.cmdloop()

    

    def do_likes(self, arg):
        likes_console = likes.likes()
        likes_console.cmdloop()



    def __bearer_oauth_followers(self, r):      

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2FollowersLookupPython"
        return r



    def __bearer_oauth_following(self, r):      

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2FollowingLookupPython"
        return r



    def __url_build(self, user_id, follows_type):
    
        following_url = "https://api.twitter.com/2/users/{}/following".format(user_id)
        followers_url = "https://api.twitter.com/2/users/{}/followers".format(user_id)
        if follows_type == "following":
            return following_url
        elif follows_type == "followers":
            return followers_url



    def __param_engine(self):

        params =   {}

        param_table = self.__conf.user_follows_params["request_params"]

        for key in param_table:
            if param_table[key] == None:
                pass
            else:
                params.update({key : param_table[key]})

        return params           



    def __retrieve_info(self, url, oauth_type):

        params = self.__param_engine()
        request = requests.get(url, params=params, auth=oauth_type)
        
        info_out = request.json()

        if request.status_code != 200:
            print("Error(s)")
            print(request.status_code)
            print(request.content)
            return
        elif request.status_code == 200:   
            if self.__conf.genopts["verbose?"]:
                print("@" + url)
            return info_out



    def __dump_info(self, json_obj, type):

        prettify = json.dumps(json_obj, indent=4, sort_keys=True)

        if type == "followers":
            with open(self.__conf.file_IO["out"]["user_follows"]["user_followers"], mode='a') as writefile:
                json.dump(json_obj, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")
        elif type == "following":
            with open(self.__conf.file_IO["out"]["user_follows"]["user_following"], mode='a') as writefile:
                json.dump(json_obj, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")

        return  
        
