# Twitter Aggregate Generator - **v.1.0.0**

## Intro:

The Twitter Aggregate Generator (Also denoted as Twitter-AG or TAG) is a program that was written as a user friendly console to gather large amounts of 
data from the official Twitter API. The intended use of this data includes, but is not limited to the following
- create a culture of accountability surrounding what politicians say on global platforms
- analyze and predict important social trends that impact day to day life
- create and analyze social networks consisting of individuals or entities of academic interest

Currently, in mere infancy, TAG only comes with modules to *gather* the desired information. However, the first major update hopes to include some modules 
for processing data. Until then users are highly encouraged to contribute data processing modules to the project for review. Additional functionalities
that are planned to be integrated soon are:
- command piping
- a small SDK 
- a compiled version of this program

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
the the named module that you are in. In this case, this is the **User Profile console**. Another prompt, say MODULE@INFO-timeline denotes the same module, but using the **Tweet Timeline** console instead of **User Profile**.

### 2. Core Functions

The core module in Twitter-AG currently has five functions/consoles (actually classes) each with a specififc API endpoint that they interface with. Similar functionality and features are similar across all functions. Some of these include full control over all request parameters, file input and output, commands, and much more. To boot and use a console, simply pass its shorthand name into the shell as a command from anywhere and it will take you there. The five consoles and their shorthands are:
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
A response for the username 'elonmusk', the current owner of Twitter with all parameters enabled would look *similar* to the one below for exmaple.

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
Besides their unique 'run' type shorthands, all consoles in the core INFO module share a set of utility commands. Some comsemands support additional arguments for additional functionality or customaization. Commands with optional args will be shown with no symbols, ex. 'list [arg]'. Commands with arguments that are required will have an asterisk before the arg, ex. 'set *[arg]'. Commands with no args will not show an argument option. The full list of commands is as follows:
- 'help' or '?' = displays the help page relevant to the current console
- 'list [arg]' = list current parameters and available commands where arg is 'commands' or 'params'
- 'set *[arg]' = utility to change a parameter where args are hierarchical dicionary keys leading to a desired parameter value, and the last arg is the value to write to the desired param 
- 'clear' = will clear the screen
- 'exit' = will terminate the current instance of Twitter-AG
Reminder - To change to a different console, simply pass its shorthand command into the shell.

### 4. Configuration:
Configuration in Twitter-AG is straightforward. The program comes with a configuration file that stores all parameters that the program will use. This file should not be edited unless you know what you are doing
