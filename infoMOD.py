import errno
import json
from time import sleep
import requests
import config_tools
import os
import sys
import cmd 
    

class user_profile(cmd.Cmd):
    """handle requests for user profiles"""


    prompt = "MODULE@INFO-user: "
    __conf = config_tools.ctools()



    def do_profile(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:
            if self.__conf.user_profile_params["read_from_file?"]:
                if self.__conf.user_profile_params["search_by_username?"]:
                    with open(self.__conf.file_IO["in"]["user_profile"]["username_list"], mode='r', ) as readfile:
                        for line in readfile:
                            request = self.__retrieve_info(self.__url_build(usernames=line.strip()))
                            self.__dump_info(request)
                elif self.__conf.user_profile_params["search_by_username?"] == False:
                    with open(self.__conf.file_IO["in"]["user_profile"]["user_id_list"], mode='r') as readfile:
                        for line in readfile:
                            request = self.__retrieve_info(self.__url_build(user_id=line.strip()))
                            self.__dump_info(request)
                return request
            elif self.__conf.user_profile_params["read_from_file?"] == False:
                if self.__conf.user_profile_params["search_by_username?"]:
                    request = self.__retrieve_info(self.__url_build(usernames=self.__conf.user_profile_params["usernames"]))
                    self.__dump_info(request)
                elif self.__conf.user_profile_params["search_by_username?"] == False:
                    request = self.__retrieve_info(self.__url_build(user_id=self.__conf.user_profile_params["user_id"]))
                    self.__dump_info(request)
            
            self.cmdloop()

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found...")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")
        
        except KeyError as key_error:
            print("UH-OH! Bad key in: " + str(key_error.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))

    

    
    def do_list(self, arg):
        print("\n__configurations__")
        param_list = self.__conf.user_profile_params
        print("\n   request_params:")
        for value in param_list:
            print("      " + str(value) + " = " + str(param_list[value]))
        files = self.__conf.file_IO
        print("\n   out:")
        for value in files["out"]["user_profile"]:
            print("      " + str(value) + " = " + str(files["out"]["user_profile"][value]))
        print("\n   in:")
        for value in files["in"]["user_profile"]:
            print("      " + str(value) + " = " + str(files["in"]["user_profile"][value]))
        print("\n")

            
        
    def do_help(self, arg):
        print("help page here!")



    def default(self, line: str):
        print("Invalid input...")
        return



    def emptyline(self):
        return
        


    def do_clear(self, arg):
        os.system("clear")



    def do_exit(self, arg):
        print("Terminating")
        sleep(2)
        sys.exit()



    def do_main(self, arg):
        os.system("python3 infoCLI.py")



    def do_timeline(self, arg):
        console = tweet_timeline()
        console.cmdloop()



    def do_tweet(self, arg):
        console = tweet_lookup()
        console.cmdloop()



    def do_follows(self, arg):
        console = follows()
        console.cmdloop()



    def do_likes(self, arg):
        console = likes()
        likes.cmdloop()



    def __param_engine(self):

        params =    {

                    }

        param_table = self.__conf.user_profile_params["request_params"]

        for key in param_table:
            if param_table[key] == None or "None":
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

        if request.status_code != 200:
            print("Error(s): ")
            print(request.status_code)
            print(request.content)
            return
            
        elif request.status_code == 200:    
            if self.__conf.genopts["verbose?"]:
                print("\nrequest @ " + url + "\n")
                print("\nResponse successful!\n")

            return info_out



    def __dump_info(self, json_object):

        try:

            prettify = json.dumps(json_object, indent=4, sort_keys=True)

            with open(self.__conf.file_IO["out"]["user_profile"]["user_profiles"], mode='a') as writefile:
                json.dump(json_object, writefile, indent=4, sort_keys=True)

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.")
        
        if self.__conf.genopts["verbose?"]:
            print(prettify)
            print("\nJSON successfully written!\n")
            return
        else:
            return    

#TODOS
# Error handling

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

class tweet_lookup(cmd.Cmd):
    
    """single tweet lookup"""


    prompt = "MODULE@INFO-tweet: "
    __conf = config_tools.ctools()


    def do_run(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:
            if self.__conf.tweet_lookup_params["read_from_file?"] == True or "True":
                with open(self.__conf.file_IO["in"]["tweet_lookup"]["tweet_id_list"], mode='r') as readfile:
                    for line in readfile:
                        self.__dump_info(self.__retrieve_info(self.__url_build(line.strip())))
            elif self.__conf.tweet_lookup_params["read_from_file?"] == False or "False":
                self.__dump_info(self.__retrieve_info(self.__url_build(self.__conf.tweet_lookup_params["tweet_ids"])))

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found...")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")
        
        except KeyError as key_error:
            print("UH-OH! Bad key in \'config.py\' : " + str(key_error.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))


    def do_list(self, arg):
        print("\n__configurations__")
        param_list = self.__conf.tweet_lookup_params
        print("\n   request_params:")
        for value in param_list:
            print("      " + str(value) + " = " + str(param_list[value]))
        files = self.__conf.file_IO
        print("\n   out:")
        for value in files["out"]["tweet_lookup"]:
            print("      " + str(value) + " = " + str(files["out"]["tweet_lookup"][value]))
        print("\n   in:")
        for value in files["in"]["tweet_lookup"]:
            print("      " + str(value) + " = " + str(files["in"]["tweet_lookup"][value]))
        print("\n")



    def do_help(self, arg):
        print("help page here!")



    def default(self, line: str):
        print("Invalid input...")
        sleep(1)
        return



    def emptyline(self):
        return
        


    def do_clear(self, arg):
        os.system("clear")



    def do_exit(self, arg):
        print("Terminating TAG...")
        sleep(2)
        sys.exit()



    def do_main(self, arg):
        os.system("python3 infoCLI.py")

    


    def do_timeline(self, arg):
        console = tweet_timeline()
        console.cmdloop()



    def do_follows(self, arg):
        console = follows()
        console.cmdloop()



    def do_user(self, arg):
        console = user_profile()
        console.cmdloop()



    def do_likes(self, arg):
        console = likes()
        likes.cmdloop()



    def __url_build(self, tweet_ids):

        id_list = "ids={}".format(tweet_ids)

        url = "https://api.twitter.com/2/tweets?{}".format(id_list)
            
        return url



    def __param_engine(self):

            params = {}

            param_table = self.__conf.tweet_lookup_params["request_params"]

            for key in param_table:
                if param_table[key] == None or "None":
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

    def __dump_info(self, json_object):

        try:

            prettify = json.dumps(json_object, indent=4, sort_keys=True)

            with open(self.__conf.file_IO["out"]["tweet_lookup"]["tweets"], mode='a') as writefile:
                json.dump(json_object, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")


        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.")


#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

class tweet_timeline(cmd.Cmd):

    """Handle requests for tweet timelines"""


    __conf = config_tools.ctools()
    prompt = "MODULE@INFO-timeline: "
    __page_count = 0
    


    def do_run(self, arg):

        print("\nRunning {}\n".format(self.prompt))

        try:        
            if self.__conf.tweet_timeline_params["read_from_file?"]:
                with open(self.__conf.file_IO["in"]["tweet_timeline"]["user_id_list"]) as readfile:
                    for line in readfile:
                        request = self.__retrieve_timeline(self.__url_build(line.strip()))
                        self.__dump_info(request)
                        self.__page_count = self.__page_count + 1
                        if self.__conf.tweet_timeline_params["pagination"]["paginate?"]:
                            while self.__page_count <= self.__conf.tweet_timeline_params["pagination"]["page_count"]:
                                self.__conf.tweet_timeline_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                                next_request = self.__retrieve_timeline(self.__url_build(line.strip()))
                                request = next_request
                                self.__dump_info(request)
                                self.__page_count = self.__page_count + 1
                            self.__page_count = 0
                        else:
                            self.__page_count = 0
                            return
            else:
                request = self.__retrieve_timeline(self.__url_build(self.__conf.tweet_timeline_params["user_id"]))
                self.__dump_info(request)
                self.__page_count = self.__page_count + 1
                if self.__conf.tweet_timeline_params["pagination"]["paginate?"]:
                    while self.__page_count <= self.__conf.tweet_timeline_params["pagination"]["page_count"]:
                        self.__conf.tweet_timeline_params["request_params"]["pagination_token"] = request["meta"]["next_token"]
                        next_request = self.__retrieve_timeline(self.__url_build(self.__conf.tweet_timeline_params["user_id"]))
                        request = next_request
                        self.__dump_info(request)
                        self.__page_count = self.__page_count + 1
                    self.__page_count = 0
                else:
                    self.__page_count = 0
                    return
        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.") 

        except KeyError as key_error:
            print("Done with " + str(key_error.args))
        
        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))



    def do_list(self, arg):
        print("\n__configurations__")
        param_list = self.__conf.tweet_timeline_params
        for value in param_list:
            print(str(value) + " = " + str(param_list[value]))



    def do_help(self, arg):
        print("Help page here")



    def default(self, line: str) -> None:
        print("Invalid input...")
        sleep(1)
        return



    def emptyline(self):
        return
        


    def do_exit(self, arg):
        print("Terminating TAG...")
        sleep(2)
        sys.exit()



    def do_clear(self, arg):
        os.system("clear")



    def do_main(self, arg):
        os.system("python3 infoCLI.py")



    def do_tweet(self, arg):
        console = tweet_lookup()
        console.cmdloop()



    def do_follows(self, arg):
        console = follows()
        console.cmdloop()



    def do_user(self, arg):
        console = user_profile()
        console.cmdloop()



    def do_likes(self, arg):
        console = likes()
        likes.cmdloop()



    def __bearer_oauth(self, r):      

        auth_key_build = f"Bearer " + self.__conf.authorization["bearer_token"]
        r.headers["Authorization"] = auth_key_build 
        r.headers["User-Agent"] = "v2UserTweetsPython"
        return r



    def __param_engine(self):

        params =   {

                    }

        param_table = self.__conf.tweet_timeline_params["request_params"]

        for key in param_table:
            if param_table[key] == None or "None":
                pass
            else:
                params.update({key : param_table[key]})

        return params           




    def __url_build(self, user_id):
            
        url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
        if self.__conf.genopts["verbose?"]:
            print("@" + url)
        return url



    def __retrieve_timeline(self, url):

        auth = self.__bearer_oauth
        params = self.__param_engine()

        request = requests.get(url, auth=auth, params=params)

        info_out = request.json()
        prettify = json.dumps(info_out, indent=4, sort_keys=True)

        if request.status_code != 200:

            print("Error(s)")
            print(request.status_code)
            print(request.content)
            return            
                
        else:
            if self.__conf.genopts["verbose?"]:
                print("@" + url)
                print(prettify)
            return info_out



    def __dump_info(self, json_obj):

        prettify = json.dumps(json_obj, indent=4, sort_keys=True)

        try:

            with open(self.__conf.file_IO["out"]["tweet_timeline"]["tweet_timelines"], mode='a') as writefile:
                json.dump(json_obj, writefile, indent=4, sort_keys=True)
                if self.__conf.genopts["verbose?"]:
                    print(prettify)
                print("JSON successfully written!")

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.")  
        
        #TODOS
        # Error handling
        # standardize and diversify info IO capability
        # add ability to add/subtract any related options for this module (especially pagination)

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

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
                        else:
                            self.__page_count = 0
                            return

            else:
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
                else:
                    self.__page_count = 0
                    return
            self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.") 

        except KeyError as key_error:
            if "next_token" in key_error.args:
                pass
            else:    
                print("UH-OH! Bad key in \'config.py\' : " + str(key_error.args))
                print("Another Tip: Read the DOCS before you break me!")

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))



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
                        else:
                            self.__page_count = 0
                            return
            else:
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
                else:
                    self.__page_count = 0
                    return
            self.__page_count = 0

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.") 

        except KeyError as key_error:
            print("UH-OH! Bad key in \'config.py\' : " + str(key_error.args))
            print("This program comes with a manual to avoid gagglef***s like this :)")


    
    def do_list(self, arg):
        print("\n__configurations__")
        param_list = self.__conf.user_follows_params
        for value in param_list:
            print(str(value) + " = " + str(param_list[value]))
        

        

    def do_help(self, arg):
        print("help page here")



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



    def do_main(self, arg):
        os.system("python3 infoCLI.py")


    
    def do_timeline(self, arg):
        console = tweet_timeline()
        console.cmdloop()



    def do_tweet(self, arg):
        console = tweet_lookup()
        console.cmdloop()



    def do_user(self, arg):
        console = user_profile()
        console.cmdloop()

    

    def do_likes(self, arg):
        console = likes()
        likes.cmdloop()



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
            if param_table[key] == None or "None":
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

        try:
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

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.")  
        

#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=#=

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
                print("Error: File not found...")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")
        
        except KeyError as key_error:
            print("UH-OH! Bad key in \'config.py\' : " + str(key_error.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))
        

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
                print("Error: File not found...")
                print("Tip: Make sure that params in 'file_IO[\"in\"]' are correct/up to date.")
        
        except KeyError as key_error:
            print("UH-OH! Bad key in \'config.py\' : " + str(key_error.args))

        except TypeError as t_err:
            print("Error: Found \'None\' in: " + str(t_err.args))
        
    
    
    def do_list(self, arg):
        print("\n__configurations__")
        param_list = self.__conf.likes_params
        for value in param_list:
            print(str(value) + " = " + str(param_list[value]))



    def do_help(self, arg):
        print("help page here!")



    def default(self, line: str):
        print("Invalid input...")
        sleep(1)
        return



    def emptyline(self):
        return
        


    def do_clear(self, arg):
        os.system("clear")



    def do_exit(self, arg):
        print("Terminating TAG...")
        sleep(2)
        sys.exit()



    def do_main(self, arg):
        os.system("python3 infoCLI.py")



    def do_timeline(self, arg):
        console = tweet_timeline()
        console.cmdloop()



    def do_tweet(self, arg):
        console = tweet_lookup()
        console.cmdloop()



    def do_follows(self, arg):
        console = follows()
        console.cmdloop()



    def do_user(self, arg):
        console = user_profile()
        console.cmdloop()



    def __param_engine(self, param_type):

        params =    {

                    }

        liking_table = self.__conf.likes_params["liking_request_params"]
        liked_table = self.__conf.likes_params["liked_request_params"]

        if param_type == "liking":
            for key in liking_table:
                if liking_table[key] == None or "None":
                    pass
                else:
                    params.update({key : liking_table[key]})
        elif param_type == "liked":
            for key in liked_table:
                if liked_table[key] == None or "None":
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

        try:

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

        except FileNotFoundError as file_error:
            if file_error.errno == errno.ENOENT:
                print("Error: File not found.\nTip: check that params for file_IO are correct/up to date.")
        except IsADirectoryError as dir_err:
            print("Error " + str(dir_err.args[0]) + ": " + str(dir_err.strerror))
            print("TIP: It is likely that your GLOBAL_FILE_PATH is incorrect OR that the a file point in file_IO params is empty!")    
