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
- **6. **

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
the the named module you are in.


