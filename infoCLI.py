# main module for TAG project
import os
import sys
import cmd
import config_tools
import infoMOD
from time import sleep

# class to handle the main console
class main_cli(cmd.Cmd):
    """main console command prompt"""

    # objects for other module's command lines to be started 
    user_mod = infoMOD.user_profile()
    timeline_mod = infoMOD.tweet_timeline()
    follows_mod = infoMOD.follows()
    tweet_lookup_mod = infoMOD.tweet_lookup()
    likes_mod = infoMOD.likes()
    # config tools is the main configuration file for anything that should not be hardcoded
    conf = config_tools.ctools()

    # visible attributes of the main console
    intro = "Main TAG console. Enter 'help' or '?' at anytime for usage."
    prompt = "MODULE@INFO:"

    # loads the user console
    def do_user(self, arg):
        print("Loading user console...")
        sleep(1)
        self.user_mod.cmdloop()

    # loads the tweet timeline console
    def do_timeline(self, arg):
        print("Loading tweet-timeline console...")
        sleep(1)
        self.timeline_mod.cmdloop()

    def do_tweet(self, arg):
        print("loading tweet-lookup console...")
        sleep(1)
        self.tweet_lookup_mod.cmdloop()

    def do_follows(self, arg):
        print("Loading user follows console...")
        sleep(1)
        self.follows_mod.cmdloop()

    def do_likes(self, arg):
        print("loading likes console...")
        sleep(1)
        self.likes_mod.cmdloop()

    # prints the help page for this console
    def do_help(self, arg):
        print(self.conf.help_pages["main"])

    # handles invalid input
    def default(self, line: str) -> None:
        print("Invalid input...")
        sleep(1)
        return

    # handles NONE input
    def emptyline(self):
        return
        
    # exits the program
    def do_exit(self, arg):
        print("Terminating TAG...")
        sleep(2)
        sys.exit()
        
    # clear the screen
    def do_clear(self, arg):
        os.system("clear")



def info_console():
    cli = main_cli()
    cli.cmdloop()

info_console()


# ____Main Project Notes____
# - refining the current pack of working infoMOD modules. Now is when to add any functionality as well
# - upload to git once once a above options are satisfied
# - 