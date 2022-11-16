# Twitter Aggregate Generator - **v.1.0.0**

## Intro:

The Twitter Aggregate Generator (Also denoted as Twitter-AG or TAG) is a program that was written as a user friendly console to gather large amounts of 
data from the official Twitter API. The intended use of this data includes, but is not limited to the following:
- create a culture of accountability surrounding what politicians say on global platforms
- analyze and predict important social trends that impact day to day life
- create and analyze social networks consisting of individuals or entities of academic interest

Currently, in mere infancy, TAG only comes with modules to *gather* the desired information. However, the first major update hopes to include some modules 
for processing data. Until then users are highly encouraged to contribute data processing modules to the project for review. Additional functionalities
that are planned to be integrated soon are:
- command piping
- a small SDK 
- a compiled version of this program
- increased access elevation and API endpoints available

To look at future modules bieng tested, take a look at the 'testing' branch for this project. To see the next update that will be pushed to 'master'
see the 'update' branch. Thank you for taking the time to check out the project!

## Table Of Contents:
- **1. Navigation**
- **2. Core Functions**
- **3. Commands**
- **4. Configuration**
- **5. Additional Information**

### 1. Navigation

Twitter-AG was built on top of the CMD python standard library for a shell style interface. The prompt for the console will tell you where you are
with a three piece pin. Take the prompt for one of the core functions as an example:
**MODULE@INFO-user: **
The first part before the '@' denotes what *type* of module you are using. Those types are:
- MODULE@ = a module that is part of the TAG core functionality
- TEST@ = a module that is currently being tested and not stable
- COM@ = a community contributed module
- DEPC@ = a module that is deprecated and will be removed with the next major update to allow time for API transition

The second part immedietaly after the '@' but before the '-' denotes the *name* of the module that you are using. In this instance the name is 'INFO'. 
This stands for information, or information gathering which is the core functionality of TAG. The last part is the function/console you are using within
the the named module that you are in. In this case, this is the **User Profile console**. Another prompt, say 'MODULE@INFO-timeline' denotes the same module, but using the **Tweet Timeline** console instead of **User Profile**.

### 2. Core Functions

The core module in Twitter-AG currently has five functions/consoles (actually classes) each with a specififc API endpoint that they interface with. Similar functionality and features are shared across all functions. Some of these include full control over all request parameters, file input and output, commands, and much more. To boot and use a console, simply pass its shorthand name into the shell as a command from anywhere and it will take you there. The five consoles and their shorthands are:
- User Profile Console = 'user'
- User Follows Console = 'follows'
- Tweet Lookup Console = 'tweet'
- Tweet Timeline Console = 'timeline'
- Likes Console = 'likes'

#### User Profile Console:
The user profile console simply retrieves a desired user profile. As a specified target, it takes either:
- a comma seperated list of usernames (no spaces)
- a single user id
- an input file of any amount of usernames/user id

For example, a response for the username 'elonmusk', the current owner of Twitter with all parameters enabled would look *similar* to the one below.

`"data": [
        {
            "created_at": "2009-06-02T20:12:29.000Z",
            "description": "",
            "id": "44196397",
            "name": "Elon Musk",
            "profile_image_url": "https://pbs.twimg.com/profile_images/1590968738358079488/IY9Gx6Ok_normal.jpg",
            "protected": false,
            "public_metrics": {
                "followers_count": 115429998,
                "following_count": 130,
                "listed_count": 101855,
                "tweet_count": 20231
            },
            "username": "elonmusk",
            "verified": true
        }
    ]`

NOTE: All response types from the Twitter V.2 API are of json type. This version of TAG only interfaces with V.2

To run the console with the currently set parameters, pass the 'profile' command to the shell. 

#### User Follows Console:
The user follows console will return two sets of data depending on which mode it is ran in. The first command, 'followers', will return a list of users who *are following* the target user id. The second command, 'following', will return a list of users that the target user id *is following*. Since both responses return user profile objects just like the **User Profile** console, all request parameters are the same as in that console. A specified target can be:
- a single user id
- an input file of any amount of user ids

This API endpoint does support pagination, which will be covered in the **Additional Information** section of this file.

#### Tweet Lookup Console:
The tweet lookup console simply returns one tweet object per request with a tweet id as a target. The target can be specified with:
- a single tweet id
- an input file of any amount of tweet ids

An example response with no parameters enabled (this response object can be massive) would look *similar* to the one below.

"data": [
        {
            "edit_history_tweet_ids": [
                "1591509211787431936"
            ],
            "id": "1591509211787431936",
            "text": "@andst7 https://t.co/ZpZ6B4F7Ou"
        },
        {
            "edit_history_tweet_ids": [
                "1591498799373258752"
            ],
            "id": "1591498799373258752",
            "text": "@westcoastbill \ud83e\uddbe"
        },
        {
            "edit_history_tweet_ids": [
                "1591490459066564610"
            ],
            "id": "1591490459066564610",
            "text": "@WholeMarsBlog Given all that is in V11, it will take a few weeks to expand the beta, then another few weeks to go wide release to US &amp; Canada"
        },
        {
            "edit_history_tweet_ids": [
                "1591487015845076996"
            ],
            "id": "1591487015845076996",
            "text": "RT @Tesla: Join our growing team installing Solar + Powerwall across the US \u2192 https://t.co/BMlhHBbAJn https://t.co/mVupmqcjiK"
        },
        {
            "edit_history_tweet_ids": [
                "1591487006508736512"
            ],
            "id": "1591487006508736512",
            "text": "RT @TeslaSolar: Tesla solar and Powerwall can power your home &amp; reduce your dependence on the grid \u2013 at the lowest price in the US \u2192\nhttps:\u2026"
        },
        
To run this console with the currently set parameters, pass the 'lookup' command to the shell.

#### Tweet Timeline Console:
The tweet timeline console will return the chronological tweet timeline for a given target user id. The response objects will be the same as in the **Tweet Lookup** console, with the same parameters available for the request. A specified target user id may be:
- a single user id
- an input file of any number of user ids

This API endpoint does support pagination. To run the console with the current set of params, pass the 'timeline' command to the shell.

#### Likes Console:
The likes console will return two possible reesponse objects depending on mode selected. The first command, 'liking', will return a list of users who *have liked* a given target tweet id. The second command, 'liked', will return a list of tweets that a given target user id *has liked*. Specified targets may be:
- a single tweet id or user id
- an input file of any amount of tweet ids or user ids

This endpoint does support pagination. 

### 3. Commands
Besides their unique 'run' type shorthands, all consoles in the core INFO module share a set of utility commands. Some commands support arguments for additional functionality or customaization. Commands with optional args will be shown with no symbols, ex. 'list [arg]'. Commands with arguments that are required will have an asterisk before the arg, ex. 'set *[arg]'. Commands with no args will not show an argument option. The full list of commands is as follows:
- 'help' or '?' = displays the help page relevant to the current console
- 'list [arg]' = list current parameters and available commands where arg is 'commands' or 'params'
- 'set *[arg]' = utility to change a parameter where args are hierarchical dicionary keys leading to a desired parameter value, and the last arg is the value to write to the desired param 
- 'clear' = will clear the screen
- 'exit' = will terminate the current instance of Twitter-AG
- 
Reminder - To change to a different console, simply pass its shorthand command into the shell.

### 4. Configuration:
Configuration in Twitter-AG is straightforward. The program comes with a configuration file that stores all parameters that the program will use. This file should not be edited unless you are setting up the program for the first time (creating defaults) or large pre-planned campaigns. Other than those two instances, it is encouraged to use the 'set' command to change variables/parameters within TAG. The 'set' command will take care of variable types and avoid unintentional mutilation of code other than the actual parameter values.

The configuration file is built using dictionaries to parameter/variable storage. Each variable has a type denoted by the comment after each dictionary item (for non programmers). Strings make up the large majority of variable types in TAG. Following are boolean and integer values. For parsing, any parameter that is of string type, and is to be omitted should have a 'None' type as its value. Any other variable type will be encoded into the request URL for the API endpoint at runtime. If a parameter is of integer type, only integers values (0-9) should be used. For boolean values, value must always be 'True' or 'False. Deviation from these rules will result in a program error or an API response error. Furthermore, any variable of string type that includes comma seperated words (parameters) should include NO spaces.

For each console in the core module there exists a dictionary named after that console in config_tools.py. This dictionary contains all of ther parameters that affect the behavior of a request. For example, there is the **User Profile** console, and in config_tools.py there is a dict named 'user_profile_params'. Additionally, there is one dictionary that is shared by all consoles called 'file_IO' in which I/O file paths are specified. A global file path parameter (not in a dict) is also included.

Using the 'set' command, the first argument will be which parameter type, or dictionary you want to edit. 
- pass 'request' to edit the request parameters
- pass 'files' to edit the shared file_IO dictionary (to change global file path pass 'global' as the next arg after 'files')

Each subsequent argument besides the last will be the **Dictionary KEY** of the parameter (or nested dict) that you wish to change. The final arg should be the value that you wish to write to said dictionary key.

As an example, let's say we wanted to set the 'max_results' parameter for the **Tweet Timeline** endpoint console to '10'. The command would look like this:

MODULE@INFO-timeline: set request request_params max_results 10

In the above command, 'set' is the command, 'request' puts into the 'tweet_timeline_params' dictionary, 'request_params' puts us into the URL encoded values dictionary, 'max_results' is the key to the value we want to change, and '10' is the value we are writing.

### 5. Additional Information:
Other than basic usage covered previosly in this reading, there are bits of additional information pertaining to the proper configuration, usage and access for TAG and/or the Twitter API. These will all be covered in this section.

#### Authorization and Access:
The twitter API uses OAuth and a pair of API keys for authenticication of requests. For the current set of core functionailty, only the OAuth bearer token from Twitter is needed for authenticication. To obtain these credentials you must sign up for a *developer* account with Twitter. Sign up is free, and no more cumbersome than signing up for an email address. Upon sign up and verification, you will be granted with all three previously mentioned credentials. Keep these safe. These keys are specific to *your* account with Twitter, and any use that violates Twitter's terms of service for the API will be solely the responsibility of the offending token's owner.

When signing up for a dev account with Twitter, there are tiers, or access levels that are available to sign up for. They are:
- essential
- elevated
- academic

TAG is currently set up to interface as an 'essential' user. The only difference between this and the 'elevated' status is better rate limites and access to a few more parameters. Once the author(s) gain better access, branches of this program will be created with those parameters in mind. Academic access is highly restricted, and will most likely not be covered by TAG. However, *if* the author(s) of TAG do ever manage to gain this access, a special branch will be created for this as well.

#### References:
Below are where you will find links to additional documention pertaining to this program or its dependencies. 
- https://developer.twitter.com/en/docs/twitter-api : This link will get you started with a dev account, docs about all types of API requests and where your personal developer dashboard will be.

#### Pagination:
Pagination is supported by the Twitter API and by TAG. Endpoints that allow/use pagination all have a dictionary for pagination controls (located in the request params) and a pagination token parameter. Assuming that you are starting a new campaign and want to start at the beginning of a data set, just switch pagination on and run the console. The program will take care of everything else and return subsequent pages until it meets the page_count parameter value. To pick up on a data set where you may have left off, simply set the pagination_token parameter to the desired token *before* running the console.

NOTE: In every response we get back from the API there is a 'next_token' key that contains a token for the following page of data. This token is what is sent back to the API in the *following* response to get the next page that we want.

### Thank You!
As always, thamk you for taking the time to check out the project! As it grows, the aim is to create something useful for the community. All contributions will be reviewed and are greatly appreciated. Check back for some BIG updated in the near future.



