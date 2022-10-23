#module to appropriately handle inputted data from infoCLI
import errno
import re
import cmd
import config_tools

class strip(cmd.Cmd):
    """will strip desired data from source"""

    prompt = "MODULE@ExIn-strip:"
    __conf = config_tools.ctools()

    def do_handle(self, arg):

        handle_re = "(?<=\@)[a-z|A-Z|\_|0-9]{0,15}"
        handle_pattern = re.compile(handle_re)

        out_file = self.__conf.file_IO["out"]["testfile"]
        in_file = self.__conf.file_IO["in"]["testfile"]
        
        try:        
            with open(out_file, mode='a') as writefile:
                with open(in_file, mode='r') as readile:
                    for line in readile:
                        match = re.findall(handle_pattern, line) 
                        if match:
                            if match.__len__() > 1:
                                for item in match:
                                    writefile.write(item)
                                    writefile.write("\n")
                            else:        
                                writefile.write(match[0])
                                writefile.write("\n")
                        else:
                            pass
            print("Done with plaintext handle strip.")

        except FileNotFoundError as err:
            print("Error: File(s) not found...")
    

strip_test = strip()

strip_test.cmdloop()
##add ability to run program with defaults or arg being the file