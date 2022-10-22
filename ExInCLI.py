#module to appropriately handle inputted data from infoCLI
import re
import cmd
import config_tools

class strip(cmd.Cmd):
    """will strip desired data from source"""

    prompt = "MODULE@ExIn-strip:"
    __conf = config_tools.ctools()

    def do_handle(self, arg):
        print(arg)


def test():
    c = strip()
    cons = c.cmdloop()

test()
