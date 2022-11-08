Program: Twitter Aggregate Generator (TAG) - v1.0.2
Author: Branden Kunkel
Email: kunkel.branden6130@gmail.com
--See 'setup.py' for all metadata and dependencies--


INTRODUCTION:

	The Twitter Aggregate Generator (TAG) was written as an easy to use, expandable, command based program to aggregate large amounts of data from the official Twitter API. Its intended purpose is to better understand social issues
facing our modern world including, but not limited to:
	
	- understanding behavior, consistency and sentiment amongst active Twitter politicians in an effort to spread a culture of accountability. 
	- put together social networks of high profile or interesting indiviuals, groups or entities.
	- seeing, tracking and predicting social trends that influence important aspects of everyday life

	The program at its current stage - v1.0.2 - is infantile and has only core functionality. This meaning that it will only procure the desired data from the API with no further processing. However, the program's current set of 
functions are powerful and simple to use. The program also allows the user to define a multitude of parameters to fine tune what the data the API responses will return. The end goal is to have a large, self contained information 
processing hub for the community to benefit from! Therefore, users are strongly encouraged to contribute to the program. Specifically, modules that make sense of the retrieved information are more in demand as there are not many API
endpoints that were not covered in this program, but will soon be. Otherwise, the first update package of data processing modules is (hopefully) coming within a month from this writing. Piping commands is also a top priority with 
the next update. For detailed usage instructions, continue reading. Thank you for taking the time to check out TAG! 





Sections:

	1) Startup
	2) Navigation
	3) Modules
	4) Commands
	5) Configuration
	6) Additional Information





Section (1) - Startup:


	The core functionalities of this program are built on top of the Python standard library 'CMD' module, making the progam immediately familiar to anyone with general terminal experience. When running infoCLI.py, you will start in 
the main command line interface. NOTE: In its current stage, the main console does not have much purpose other than to be an entry point into the program. However, is was put there anticipating further expansion. From this interface you 
can choose which console to direct to. Each 'console' in TAG is actually a class, built on top of 'CMD' that has a specific Twitter API endpoint that it handles. For the purpose of this reading, the words 'modules' and 'consoles'
shall be used interchangeably. You will be greeted with version number, and an intro that looks similar to "Main TAG console. Enter 'help' or '?' at anytime for usage.". Also make note of the prompt. This will appear 
as a prompt before your cursor in every console. This will look like "MODULE@INFO: " in the main console. 





Section (2) - Navigation:


		Navigation of the program and its various consoles is straightforward. The prompt in TAG acts as a pin for what module you are in. The prompt has a hierarchy similar to a directory. The first part before the '@'
 denotes that you are in a working core module. Modules that are in testing, need fixed, or are NOT a part of the core functionailty will present different identifiers before the '@' symbol. Anyone who contributes a module to the
program is urged to follow this ruleset, as contributed code will be changed to accomodate them regardless. These labels are as follows:
	
			MODULE@ = denotes a working core module
			TEST@ = denotes a core module that is under testing or not stable
			EXT@ = denotes a module that is not part of core functionailty (contributed by someone other than the original author(s))
			DEP@ = denotes a deprecated module that is scheduled for deletion, but still included for time to migrate to a suitable replacement

	The second part to the pin, after the '@' symbol but before the hyphen '-', indicates which collection of modules you are in. At the time of this writing, there is only one section - 'INFO'. This collection of modules are part of 
the core features that actually retrieve and dump the desired information. The next collection of modules will have a seperate identifier in this postition, and so on for all added collections. Finally, in the last position, after the 
hyphen is the sub id. This denotes what module you are currently using within a given collection. So, if you were working inside of the 'user profile' module under the 'INFO' collection, your prompt would look like this:

			MODULE@INFO-user:
	
Another example could be that you are in the tweet timeline module rather than the user profile module. In this case your prompt would look like:

			MODULE@INFO-timeline: 

Knowing this three piece pin will allow you to easily identify where you are and where you want to go. Furthermore, you can switch between modules by simply passing thier shorthand name as a command. For example:

			MODULE@INFO-user: timeline > ENTER will put you into the tweet timeline console (MODULE@INFO-timeline) from the user profile console. To go back to the user profile console - MODULE@INFO-timline > ENTER.
	
All current working core modules and their shorthand command are as follows:
			
			user profile - user
			user follows - follows
			tweet timeline - timeline
			tweet lookup - tweet
			likes - likes
		
	*The next section will focus on each module and its capabilities. As previously mentioned above further modules are on their way, and for future reference will be updated into this help page as they come.
			
	 



Section (3) - Modules:


	QUICK START NOTES:
		
		- All response objects from the API are of JSON type. They are serialized and derserialized accordingly using the json python standard library.
		- Pagination refers to obtaining data within multiple sequential pages. This is achieved via a pagiantion key present in some response types.
		- All modules output to .json files for easy, standardized transfer of data by default. Specification of other
		- All modules use the config.py file for run configurations.
		- All modules support a read from file option for usernames, user ids or tweet ids. Each line should contain only one of the proviously mentioned strings with no other characters. 


User Profile Module:
		
	The user profile module is the most straigtforward module of the current set of working core modules. It simply fetches the desired user profile object based on username or user id#. Requests made with usernames may  		
be made with multiple usernames per request or just one. For multiple usernames, this can only be a comma seperated list (no spaces) of usernames which the program will encode into the request URL at runtime. 
Alternatively, you can use the read from file parameter to pass the module any number of usernames easily. As stated in the quick start notes, each line in a read file should contain only one username, user id or tweet id with 
no other characters. Although most modules will ONLY support this input structure, and for uniformity you SHOULD follow this input structure; for requests with usernames in this module only, each line in a read file may contain a 
comma seperated list (no spaces) of usernames if desired. You can also search a user profile with a given user id. This request DOES NOT support multiple user ids per request. Instead, if you wish to search more than one profile via 
user id, you must use a read file.
	To run the user profile module with the current parameters, simply pass the command 'profile' into the console. All other commands will be discussed futher in another section. Available request paramaters for the user profile
module and their return values are as follows:

		user.fields: 
			"description" = user's profile description
			"id" = user's user id
			"public_metrics" = returns public metrics (if available) on the given profile
			"created_at" = date the profile was created
			"entities" = twitter entities mentioned - see twitter docs to learn more about entitites
			"location" = user's last updated location
			"name" = user's name (user can make this up)
			"profile_image_url" = URL to the user's profile picture 
			"protected" = True or False to wether profile is protected
			"url" = unique profile URL
			"username" = twitter handle
			"verified" = True or False to wether user is verified
			"withheld" = withheld information
		expansions:
			 "pinned_tweet_id" = user's pinned tweet identification number


User Follows Module:

	The user follows module will return a list of user profiles just like the User Profile module for either A). The users that ARE FOLLOWING the given user id, or B). The users that the given user id IS FOLLOWING. This module will
only accept user ids, NOT usernames. If a username is given, the Twitter API will return an error message that will be printed in the console for you to reference. Furthermore, only one user id may be given per request. If you wish to
gather large sets of data for multiple user ids, use the read from file function of the module (all modules currently support this feature). The User Follows Module has two 'run' commands - followers and following.
		
		- passing 'following' as the command into this console will return pages of users that the given user id is following. 
		- passing 'followers' as the command into this console will return pages of users that are following the given user id.
	
	This module does support pagination of requests, which will be covered in depth in the configuration section. Available request parameters and their return values are the same as in the User Profile module, as this module
still returns user profiles, just within a different context.



Tweet Lookup Module:

	The tweet lookup module is another straightforward module to use, albeit there are many more request parameters and return values to work with. This module will return a tweet object - the very foundation of Twitter.
Tweet objects can potentially contain a very large amount of data as opposed to user profiles. Information such as who created the tweet, when, who was mentioned, what entities were mentioned, who liked the tweet, and much much more.
The tweet lookup module simply needs a tweet id as a target. All tweets, and tweets within a tweet (conversation) will have a unique id number, which is the only way to find said specific tweet. Only one tweet id may be sent per request. 
As usual, however, you can run a large campaign using the read from file feature. The available request parameters and return values are as follows:

		expansions: 
			"attachments.poll_ids" = list of poll ids present in the tweet
			"attachments.media_keys" = information about media present in the tweet
			"author_id" = uder id of the tweet's author
			"edit_history_tweet_ids" = tweet id's of edited tweets (when you edit a tweet, it gets a new tweet id)
			"entities.mentions.username" = usernames mentioned in the tweet 
			"geo.place_id" = place tagged in the tweet
			"in_reply_to_user_id" = user id of the user being replied to in the tweet
			"referenced_tweets.id" = tweet ids of tweets referenced in the tweet
			"referenced_tweets.id.author_id" = user id of the author of a mentioned tweet
		media.fields: 
			"duration_ms" = duration of media in milliseconds 
			"height" = pixel height
			"width" =  pixel width
			"media_key" = key
			"preview_image_url" = image url
			"type" = media type
			"url" = media URL
			"public_metrics" = various public metrics 
			"non_public_metrics" = RESTRICTED ACCESS
			"organic_metrics" = RESTRICTED ACCESS
			"promoted_metrics" = RESTRICTED ACCESS
			"alt_text" = alternative text
			"variants" = variants
		place.fields:
			"contained_within" = physical boundary of tweet
			"country" = country of origin
			"country_code" = country of origin code
			"full_name" = full name of place
			"geo" = coordinates of place
			"id" = place id
			"name" = place name
			"place_type" = place type
		poll.fields:
			"duration_minutes" = poll duration
			"end_datetime" = end time for po;;
			"id" = poll id
			"options" = poll options
			"voting_status" = votes
		tweet.fields:
			"attachments" = included attachments
			"author_id" = user id of tweet author
			"context_annotations" = annotions about tweet context
			"conversation_id" = id of conversation that the tweet may be part of
			"created_at" = when tweet was created
			"edit_controls" = edit controls
			"entities" = list of entities
			"geo" = coordinates
			"id" = tweet if
			"in_reply_to_user_id" = user id of user the tweet if replying to 
			"lang" = language the tweet is written in
			"public_metrics" = various public metrics
			"possibly_sensitive" = True or False on if info could be sensitive
			"referenced_tweets" = tweet ids of referenced tweets in the tweet
			"reply_settings" = setting for replies
			"source" = source
			"text" = tweet text
			"withheld" = withheld information



Tweet Timeline Module:

	The tweet timeline module produces tweet objects just like the Tweet Lookup module but in the form of a target user's chronological tweet timeline. The Twitter API will allow the request to go back as far as 3200 tweets per user.
This module takes user ids as the target identifier, with one user id per request. Using pagination in conjunction with the read from file feature, you could possibly acquire the most recent 3200 tweets from as many users as desired 
assuming you don't reach your data cap. Data caps will be discussed in depth later, but was mentioned here due to the fact that this module is usually the most data consuming one that you will use. For quick reference, for essential
access to the API (access priviledge will also be discussed) you are allowed 500,000 tweets per month. Assuming you have not used any of the current month's data, you could pull 3200 tweets for about 156 users (500,000 / 3200 = 156.25).
To run the tweet timeline with current configurations, pass 'timeline' as a command into the console. The request parameters are the exact same as with the tweet lookup console, with a couple of added parameters, which are:


			exclude = exclude unwanted information, such as re-tweets.
			start_time = timestamp of the date you wish to start the timeline from.
			end_time = timestamp of the date you wish to end the timeline from.
			until_id = specifies the tweet id at which the timeline will stop.



Likes Module:

	The likes module will return information about either A). Which users liked a given tweet or B). Which tweets a given user has liked. 
		
		- pass 'liking' as the command to see who has liked a given tweet
		- pass 'liked' as the command to see which tweets a given user has liked
	
	Available request parameters and return values are the same as in previous modules for both types of run commands. Since liking will return user profiles of those who liked a given tweet, the params and return values will be
the same as in the User Profile module. Alternatively, since liked will return which tweets a given user has liked, the params and return values will be the same as in the Tweet Lookup or Tweet Timeline modules.
		




Section (4) - Commands:


	Besides their respective 'run' type commands for each module, there is a list of commands which are found in most core modules. These commands are utilities that perform standard actions such as 'exit' or
update parameters during run time. These commands are listed below. To aid in comprehension, anything contained within the single quotes ('') is the verbatim command. Anything contained within the square brackets ([]) denotes an argument
or command which is not explicitly defined/optional, i.e 'list [arg]' could be 'list params' or 'list commands' or 'list' (arg ommitted). If the square brackets are preceeded with an exclamation mark (![arg]), then the argument is not 
optional and must be passed along with the command. If the square brackets are followed by an asterisk ([arg]*), then that means that there are optional arguments after the one marked with (*). Lastly, if the square brackets are followed by both 
an exclamation point and an asterisk ([arg]*!), then that means that there are additional arguments, but they are NOT optional. 
	So, hypothetically:

		- 'cmd' means just that command
		- 'cmd [arg]' means 'command with one optional argument
		- 'cmd [arg]* means 'command with multiple optional arguments 
		- 'cmd ![arg]' means 'command with one required argument
		- 'cmd ![arg]*' means 'command with multiple arguments, the first argument being required and every one after being optional
		- 'cmd ![arg]*!' means 'command with multiple arguments, all of them being required 

	Commands:

		- '[run command]' - the module specific command to retrieve the desired information

		- 'list [arg]' - will print the entire list of parameters and commands for a given module
			- if arg = 'params': will print only the given module's parameters
			- if arg = 'commands': will print only the given module's commands
		
		- 'set ![arg]*! - utility command to set parameters from the console
			- all arguments for this command are required. Simply passing 'set' or 'set' with incorrect amount of arguments will result in a waste of time (Errors)
			- parameter configuration will be covered in depth, as will the 'set' utility. A brief and memory-jogging explanation will be provided here
			- the first argument will dictate which set of parameters you wish to make edits to.
				- if arg = 'request': will move to edit parameters pertaining to the information request
				- if arg = 'files': will move to edit which files will be used for I/O
				- if arg - 'global': will move to edit the global file path
			- the next argument will either be the key to the value you wish to change, or a key to another parameter dictionary to edit
			- every other following argument will either be  a key to a value you wish to change, key to another parameter dictionary, or the actual value you wish to write to the given param, depending on where you
				are in you dictionary tree. (trees and dictionaries will also be covered in the configuration section)
		
		- 'clear' - will clear all text from the screen and set a new prompt
		
		- 'help or ?' - will print the help page specific to the current working module

		- 'exit' or Ctrl + z ' - will exit the current running instance of the program

		- as mentioned in the Navigation section, passing any module's shorthand name into any module's command line will direct you to that module. Module names and thier shorthands are as follows:	
			
			user profile - 'user'
			user follows - 'follows'
			tweet timeline - 'timeline'
			tweet lookup - 'tweet'
			likes - 'likes'





Section (5) - Configuration:
	

	In previous sections, small examples and some parameters referred to as 'request parameters' or 'parameters' were overviewed. This section describes the options for setting parameters, types of parameters, what they do and 
any relevant information. For the purpose of consistency and learning this program, certain parameter groupings must be defined. From here on, 'parameters' will refer to any program runtime value that can be changed by a user.
'request parameters' will refer to any parameter that changes the behavior of a request(s). 'file parameters' will refer to any parameter that changes the I/O stream of a module. If you are beyond the most novice programmer,
then skipping this section is up to you.
	
	Included in the program is a file called config.py. This file is a critical component of the program where all values that the program uses are stored. These values are also what the user will be changing to suit their needs.
Values for this program are all stored in data sets called Dictionaries. Dictionaries are simple and easy to read by humans and computers, which is they were used. They are simply key:value pairs where key is the name of the value,
and value is what the key contains. These values are what we have been calling parameters, and are actually called variables. Dictionaries can also be nested. This means that a dictionary can have a dictionary as a :value 
to a key: along with other variables. This dict within a dict can also have yet another dictionary as a :value and so on. An example of this structure from config.py:

		user_profile_params =   {       
                                        "usernames" : None,

                                        "user_id" : None,

                                        "search_by_username?": True,

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld",
                                                                        "expansions" : "pinned_tweet_id",
                                                                },

                                        "read_from_file?" : False,               
                                }

	Anything contained within the curly ({}) brackets and divided by the colon (:) is a key:value entry in a dictionary. As you can see, 'user_profile_params' is indeed a dictionary. The first entry is a simple key:value pair 
where key is 'usernames' and value is 'None'. If we look further down to 'request_params' we can see that this key:value pair is request_params:dictionary. This is a nested dictionary. Inside of the 'request_params' dictionary, 
you can see more key:value pairs. Dictionaries can be nested infinitely in theory. However, this program has much less nesting than that. This example is showing the parent dictionary as 'user_profile_params'. There are parent 
dictionaries named after each module that look similar to the one above. Each of the above parameters/values/variables will affect the behavior of a request and are therfore grouped into this dict. 
	
	To change a parameter in the config.py file, simply change the VALUE of the desired key:value pair. For example, to change 'usernames' to Elon Musk's username, change 'None' to 'elonmusk'. Or if you wish for the module 
to read usernames/user ids from a file, change the key:value pair 'read_from_file?': 'False' to 'read_from_file?' : 'True'. Now, even though we dubbed these parent dictionaries as request parameters, surely you've noticed the 
'request_params' key inside of the parent dictionary. These were named, or not named rather, to keep confusion out of the actual program developement although seemingly backwards. The key:values inside of the 'request_params' dictionary 
are the parameters that are actually SENT and encoded into the request URL. To clarify, when refering to 'request parameters', this reading is referring to the module named parent dictionary like the one above. It is also important 
to note that these particular parameters present in every module's request parameters parent dictionary and are responsible for what information that you get back. Leaving these empty will result in simple and undisclosing default 
return values from the API. NOTE: Read the in depth explanation of the 'set' command further down in this section before you go touching the config.py file!   

Now that we have covered the basics, let's look at another example:

		GLOBAL_FILE_PATH = ""

		file_IO =       {
                                "out" : {

                                                "user_profile" :        {
                                                                                "user_profiles" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "tweet_timelines" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_followers" : GLOBAL_FILE_PATH + "",

                                                                                "user_following" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweets" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "likes" :       {
                                                                        "liking" : GLOBAL_FILE_PATH + "",
                                                                        "liked" : GLOBAL_FILE_PATH + "",
                                                                },
                                                
                                        },

	Here we have another variable, a dictionary, called 'file_IO'. This dictionary is where parameters dubbed 'file parameters' are stored. The structure is the same as in the previous example, except with two nested
dictionaries. Additionally, unlike the unique request parameter dictionaries, all modules share the 'file_IO' dictionary. 'file_IO' is the parent dict, 'out' is the first key entry which also a dictionary. Finally here we will 
find our key:value pairs we were searching for. 'out' dict is where we should specify the output files for each module. There is another dict,  'in', not shown here that specifies what files each module will read from. Note the 
variable above our file parameters called 'GLOBAL_FILE_PATH'. This is where you should specify a path to where your IO files are stored. They can be anywhere that you want. If the files are in the same path as this program, then this 
parameter is not needed. However, it is probably wise to keep them somewhere else. Unlike most values in key:value pairs, to change parameters in this dict, you must change only part of the value in the key:value pairs. For example, 
take "tweet_timelines" : GLOBAL_FILE_PATH + "". If you change anything other than what is inside of the quotation marks, then the program will no longer be able to recognize where to look for files.

	The last thing to cover before we dive into actually writing the configurations is variable types. For every key:value pair in a dictionary, the key is simply a string that is used to identify the desired value. The value 
is actually what we know in programming as a variable. We have been referring to them as parameters or values for the most part, which they are for the user's intents and purposes. However, it is important to understand the concept 
of variable TYPES in order to properly use this program. Common types of variables include:
		
		- string = plain text, generally encoded with ASCII or UTF-8 (linux)
		- integer = a whole number, not text.
		- floating point integer = decimal number, not text
		- boolean = simply True or False
		- None = varibale has NO type
	
	Strings in this program's config files will ALWAYS be encapsulated within "" or ''. They both mean string. Other variable types, like an integer, will NOT have quotes of any kind around them. i.e "5" is a string of plain text,
where 5 is an integer. Another example; "True" is plain text that says 'True', where True is a boolean type (no quotes). Almost all variable types in TAG will be strings. 
	There are comments in config.py (anything after the pound '#') that will denote the type of variable for each parameter, or variable. Using variable types that do not match the default type will result in errors or undefined 
behavior. let's look at yet another example. Take a moment to look over the example from the Likes module's request parameters. You will see types of string, None, True, False and integer. 

		likes_params =  {
                                "read_from_file?": True, # boolean

                                "tweet_id" : None, # string

                                "user_id" : 12345, # string

                                "pagination" :  {
                                                        "paginate?" : False, # boolean
                                                        "page_count" : 2, # integer
                                                },

                                "liking_request_params" :       {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                        "max_results" : "5", #string
                                                                        "pagination_token" : None # string
                                                                },

                                "liked_request_params" :        {    
                                                                        "expansions" : "attachments.poll_ids,attachments.media_keys,author_id,edit_history_tweet_ids,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id", # string
                                                                        "max_results" : "5", # string
                                                                        "media.fields" : "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,non_public_metrics,organic_metrics,promoted_metrics,alt_text,variants", # string
                                                                        "place.fields" : "contained_within,country,country_code,full_name,geo,id,name,place_type", # string
                                                                        "poll.fields" : "duration_minutes,end_datetime,id,options,voting_status", # string
                                                                        "tweet.fields" : "attachments,author_id,context_annotations,conversation_id,created_at,edit_controls,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
                                                                        "pagination_token" : None, # string
                                                                        "exclude" : None, # string
                                                                        "start_time" : None, #string
                                                                        "end_time" : None, # string
                                                                        "until_id" : None, # string
                                                                },
                        }

	As you can see, the comments after each variable indicate what variable type it should be. You probably also will have noted that where comments indicate that the type should be string, there is None in it's place. This is
because for any string type parameter that you do NOT want to use, the value should be of None type. If if quotes are used, even if empty, the program will still load them in for runtime. If the value is None, the program knows to skip
loading that parameter. For integer variable types, you should use only integers as values (0-9*). For boolean variable types, only True or False variable types should be used. Also note that in ANY string type parameter in the 
config file, there SHOULD NOT be any spaces within the string. Not at the beginning, after puncuation(commas), or at the end.
	
	Knowing all of this fundamental information and how to edit the config.py file is a must. However, directly editing the configuration file is both risky and cumbersome. The risk being that if you erase, change or otherwise
disrupt the framework of this file, the program will break. You will then have to download another unmutilated config.py file from the repository and re-write all desired defaults. Additonally, every time you run an instance of TAG, 
all of the information in this file will be loaded into memory. This means that even if you change a parameter in the file while TAG is running, it will not recognize the changes until they are saved to the file and the program is 
re-started. This is fine for large, preplanned campaigns for which you went through and changed all variables in the file to suit your needs, but still not efficient and certainly not okay for those times you go to run the program and 
realize that you screwed up one variable. This is why the super awesome 'set' command was written. Using this command, you can change parameters on the fly, while the console is running and without having to worry about ruining the
configuration file. All values that the user writes will automatically be converted to the correct type and the parameter will be updated in memory. This is much better for obvious reasons, as well as not so obvious ones. For instance,
you can carefully edit the config file with the defaults you want, and they will stay that way. This is because parameter updating happens ONLY in memory with the set function. Additionally, parameters updated in memory for one
module will not be erased from memory when switching to another module. If you change some params in the User Profile module for example, then switch to the tweet timeline module, do whatever and then come back to the user profile module, 
your parameters will be the same as when you left. This is true for all modules, and does not change regardless of how many times you switch modules until the program is terminated. At that point, parameters changed in memory,
i.e with the set function will be erased from memory. Rebooting will load the default hard coded parameters from the config.py file.
	
The set command was briefly covered with a fairly thorough example. However, usage can be hard to explain in a couple lines of text, so here is a full guide to the set command along with a working example.


		
                        }

		file_IO =       {
                                "out" : {

                                                "user_profile" :        {
                                                                                "user_profiles" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "tweet_timeline" :      {
                                                                                "tweet_timelines" : GLOBAL_FILE_PATH + "",
                                                                        },

                                                "user_follows" :        {
                                                                                "user_followers" : GLOBAL_FILE_PATH + "",

                                                                                "user_following" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "tweet_lookup" :        {
                                                                                "tweets" : GLOBAL_FILE_PATH + ""
                                                                        },

                                                "likes" :       {
                                                                        "liking" : GLOBAL_FILE_PATH + "",
                                                                        "liked" : GLOBAL_FILE_PATH + "",
                                                                },
                                                
                                        }, 

	Above are the request parameters for the Likes module, along with the shared files parameters. From earlier, the set command template is 'set ![arg]*!'. Every argument is required. The amount of arguments depends of how
many nested dictionaries there are in the current group of parameters. The first argument will indicate which group of parameters you wish to change (files parameters, request parameters, global file path). Each group has a shorthand
name to pass as an argument to reach that group. These are:

		- files parameters = 'files'
		- request parameters = 'request'
		- global file path = 'global'

Every command after the first and up until the last one are going to be dictionary keys leading to the parameter you wish to change, with the last argument being the value that you wish to write to the desired parameter. All arguments 
must be seperated by a space. So, remembering our variable types, if I wanted to change the request parameter 'tweet_id' from None to 12345, the command would be: 'set request tweet_id 12345'. 'set' is the command to use the function, 
'request' is the shorthand for the request parameters dictionary group (second argument), 'tweet_id' is the exact name of the key:value pair we want to edit (third argument), and '12345' is the value that we are writing (last argument).
	Lets assume instead that we want to change the 'max_results' parameter in the 'liking_request_params' dict which is in the Likes module's request parameters. This command would be: 
'set request liking_request_params max_results 15' 
One more example. Assume we want to change where this module outputs the information it receives. To do this, we need to reach the 'liking' parameter which is in the 'likes' dict, which is in the 'out' dict which is in turn inside of the
files parameters group 'file_IO'. For this, we will do two commands. One to set our global file path and one to change the output file. The first command would be 'set global /home/madeupuser/Documents/TAGdocs'. This directory is where
we hypothetically stored all of these files. The second command would be : 'set files out likes liking likingusers.txt'.

As you can see, using this function is simply following dictionary keys down the tree until you reach the desired parameter! 
	




Section (6) - Additional Information:


To preface, thank you for taking the time to read this far, and for checking out the program! Many more cool functionalities are in progress. I also encourage users to contribute modules to the code! 

This section is intended to provide extra help and information about the program that was deemed to verbose or sidetracking to stick in previous sections. This includes rate limiting, access levels, authentication, pagination
	and more!


PAGINATION:

	Pagination was touched on but not elaborated about. Here we will describe the process and options more carefully. Pagination is used when the information you requested will not fit on one page (exceeds max_results highest #).
The information from page to page will be in sequence (chronological). For every request sent we get a response. In the response data, there exists a 'next_token' parameter. When this token is sent in the next request as the 
pagination_token parameter, the API refers to the token to know what page it should send next. For new data campaigns, we usually want to start at the beginning of a data set. To do this for supported API endpoints, simply set the 
'paginate?' parameter as True. The program will take care of finding and sending pagination tokens up until the desired stopping point. Pagination behavior is dependent on some extra parameters. The first one, in the same dict as 
'paginate?', is 'page_count'. This is an integer that sets how many pages of information to gather. So if 'page_count':10, then the program will return 10 pages of information. The other is the 'max_results' parameter. This number 
(actually string type) dictates how many results you will get per page. NOTE: Number must be in the range 5-100. Any other value will return an error message in the API response. Knowing this, we can precisely control how many 
results we will get in total. Take this example:

		 user_follows_params =   {
                                        "read_from_file?" : False, # boolean

                                        "user_id" : "123456789", # string

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                        "max_results" : "10", # string
                                                                        "pagination_token" : None # string
                                                                },

                                        "pagination" :  {
                                                                "paginate?" : True, # boolean
                                                                "page_count" : 10 # integer

	This configuratioin will return exactly 100 results divided between 10 pages. 'paginate?' = True, 'page_count' = 10, 'max_results' = 10. 10 x 10 = 100
Now say we ran a campaign earlier in the week, but needed to wait for our rate limit to refresh, so we came back to it. We would not want to start back at the beginning of our data set and waste our rates on data already gathered.
So, this where writing in a pagination token before running the module would make sense. If the above example looked like the one below, then we the program would run with the same behavior as above, but it would start right where
we left off. This is because before we shut down after our earlier hypothetical campaign, we took the last 'next_token" that we recieved, and directly wrote it to the 'pagination_token' parameter for this module, and saved. So when the 
program next boots up and loads the config.py file, it will see that there is indeed a pagination token we should send with the request (which in this case if our first request of the session). This token will tell the API where 
we left off. If you are not picking up at a previously left spot, then leave this parameter empty.
		
		 user_follows_params =   {
                                        "read_from_file?" : False, # boolean

                                        "user_id" : "123456789", # string

                                        "request_params" :      {
                                                                        "user.fields" : "description,id,public_metrics,created_at,entities,location,name,profile_image_url,protected,url,username,verified,withheld", # string
                                                                        "expansions" : "pinned_tweet_id", # string
                                                                        "max_results" : "10", # string
                                                                        "pagination_token" : 12k4jh83254gh3254i87ghhhh # string
                                                                },

                                        "pagination" :  {
                                                                "paginate?" : True, # boolean
                                                                "page_count" : 10 # integer

ACCESS LEVELS/AUTHENTICATION:

	To access the Twitter API, you must sign up with a developer account. Signing up will provide you with the credentials needed to access the API. There are three access levels for the API. Essential, elevated and academic.
Academic access requires credentials from an academic institution with good standing. This is the only way to get this access to my knowledge, and this version of TAG was not written for this access level. Elevated access simply requires
additional application, is free and allows mostly for better rate limits. Essential access is the lowest access level, but still provides a mass amount of available information. This program was written with essential access. In the 
future, a release will be provided for those with advanced access levels. This will come when the author recieves this access, as I can't test the program without making real requests.

	Twitter will give you a set of credentials upon sign up and verification. These are the Bearer Key, API Key, and API Secret key. Do not lose these or you will have to apply and be sent new creds. Furthermore, this program does 
NOT include any of these credentials. You must sign up and obtain your own (sign up is free and easy) credentials, as they are issued individually per account. This means that any program use or data use that goes against Twitter's
API usage policy will be be the responsibilty of the individual. Consequences from violating these terms and conditions are not my responsibility, and may result in an account ban.
The credentials that you get should be hard coded into the 'authorization' dictionary in config.py as STRINGS and then be left alone. There is no 'set' function for the authorization dict, because you should rarely, if ever, have to
change these values.



RATE LIMITS:

	Any developer account with Twitter has a tracked rate limit for how many requests you can make within a given timeframe. Furthermore, different response objects have different rate limits. for example, the limit for tweets
and the limit for users if different. Instead of listing all rate limits here, I have provided a link to the proper Twitter docs due to the sheer size of this list.

			https://developer.twitter.com/en/docs/twitter-api/rate-limits



ERRORS:
	This program comes complete with error handling for pre-defined user mistakes. If you use this program and encounter a traceback, please Email the issue to the author's email listed at the top of this page.
Errors are divided into two kinds in this program. Program errors, and API errors. A program error happens when something is wrong within our local program code. API errors are handled by the Twitter API and are sent back as
responses when something breaks. A program error could be a missing file for example, and would look similar to this snippet:
						
							       "listed_count": 35,
							"tweet_count": 197
						    },
						    "username": "none",
						    "verified": false
						}
					    ]
					}

					Response successful!

					Error: File not found.
					Tip: check that params for file_IO are correct/up to date.
					MODULE@INFO-user: 

	Alternatively, an API error could be caused by having an incorrect range in 'max_results' i.e 'max_results' : '0'
This error message would be from the API, and would look something like this snippet:

					Running MODULE@INFO-timeline: 

					Error(s)
					400
					b'{"errors":[{"parameters":{"max_results":["0"]},"message":"The `max_results` query parameter value [0] is not between 5 and 100"}],
					"title":"Invalid Request","detail":"One or more parameters to your request was invalid.","type":"https://api.twitter.com/2/problems/invalid-request"}'

Most error messages will contain tips or a push in the right direction to try and solve the problem based on common mistakes.




NOTES:
	For people with weak or no typing skills, this program may feel cumbersome. Although if you cant type, many information technology tools may feel this way. I personally encourage users to learn to type. A week of practice will 
change your life! :) For those poor souls, however, the consoles in this program have a cool feature that can help with this. This feature is command memory. Every command that you enter will be saved and can be reused to cut down
on typing. Lets say we are in the user profile console, and we enter three commands while we work:

		MODULE@INFO-user: set files out user_profile user_profles something.txt
		MODULE@INFO-user: set request usernames elonmussk
		MODULE@INFO-user: profile
	
	Here you can see that we changed a file parameter, changed a request parameter and then tried to run the module. Uh-oh, we got a program error! It seems that we misspelled 'user_profiles' like 'user_profles'. We can either
retype that whole set command, which is quite long, or we can press the down arrow key! Pressing the down arrow key will stage the previosly entered command for entry. Consecutive presses will keep cycling back further through commands, 
staging each one for entry. Here, if we press the down key three times, we can stage that long command and then just edit the part that we screwed up. Like this:

		Down key press no.1 - MODULE@INFO-user: profile
		Down key press no.2 - MODULE@INFO-user: set request usernames elonmussk
		Down key press no.3 - MODULE@INFO-user: set files out user_profile user_profles something.txt - On press no.3 we end up with this prompt. 
		
	Now we can simply use the cursor to edit that command to look like this:
		
		MODULE@INFO-user: set files out user_profile user_profiles something.txt 
	
	Then we just press enter. Viola! We fixed our mistype without having to type that long string out all over again, hopefully with no mistakes.




__________________________________________________________________________DONE!! This is the end. Thanks again for reading!_________________________________________________________________________________________________________________________











		 
