# main module for TAG project
import os
import sys
import cmd
import config_tools
import infoMOD
from time import sleep

version = "v.1.0.1\n"

class main_cli(cmd.Cmd):
    """main console command prompt"""
 
    user_mod = infoMOD.user_profile()
    timeline_mod = infoMOD.tweet_timeline()
    follows_mod = infoMOD.follows()
    tweet_lookup_mod = infoMOD.tweet_lookup()
    likes_mod = infoMOD.likes()
    conf = config_tools.ctools()

    intro = version + "Main TAG console. Enter 'help' or '?' at anytime for usage."
    prompt = "MODULE@INFO:"

    def do_user(self, arg):
        print("Loading user console...")
        sleep(1)
        self.user_mod.cmdloop()

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

    def do_help(self, arg):
        print(self.conf.help_pages["main"])

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



def info_console():
    cli = main_cli()
    cli.cmdloop()

info_console()
