#! usr/bin/env python
import twitterag.user_profile as user_profile
import twitterag.user_follows as user_follows
import twitterag.tweet_lookup as tweet_lookup
import twitterag.tweet_timeline as tweet_timeline
import twitterag.likes as likes
import twitterag.config_tools as config_tools
import os
import sys
import cmd
from time import sleep

version = "v.1.0.2\n"

class main_cli(cmd.Cmd):
    """main console command prompt"""
 
    user_profile_console = user_profile.user_profile()
    user_follows_console = user_follows.follows()
    tweet_lookup_console = tweet_lookup.tweet_lookup()
    tweet_timeline_console = tweet_timeline.tweet_timeline()
    likes_console = likes.likes()
    conf = config_tools.ctools()

    intro = version + "Main TAG console. Enter 'help' or '?' at anytime for usage."
    prompt = "MODULE@INFO:"

    def do_user(self, arg):
        self.user_profile_console.cmdloop()

    def do_timeline(self, arg):
        self.tweet_timeline_console.cmdloop()

    def do_tweet(self, arg):
        self.tweet_lookup_console.cmdloop()

    def do_follows(self, arg):
        self.user_follows_console.cmdloop()

    def do_likes(self, arg):
        self.likes_console.cmdloop()

    def do_help(self, arg):
        print("help page here")

    def default(self, line: str) -> None:
        print("Invalid input...")
        sleep(1)
        return

    def emptyline(self):
        return
        
    def do_exit(self, arg):
        print("Terminating")
        sleep(2)
        sys.exit()

    def do_clear(self, arg):
        os.system("clear")

    def do_list(self, arg):
        print("\nAvailable modules:")
        print("     user")
        print("     timeline")
        print("     tweet")
        print("     follows")
        print("     likes")



def main():
    cli = main_cli()
    cli.cmdloop()

main()
