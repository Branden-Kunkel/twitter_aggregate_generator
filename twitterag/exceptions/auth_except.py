## Author created exceptions go here##

class ShellArgError(Exception):
    """exception for when a shell argument is not in scope"""
    
    def __init__(self, shell_argument):

        self.shell_arg = shell_argument

    def __str__(self) -> str:
        
        return(repr(self.shell_arg))


class ParamTypeError(Exception):
    """exception for invalid parameter (config) variable types"""
    
    def __init__(self, parameter):
        
        self.parameter = parameter

    def __str__(self):
        
        return(repr(self.parameter))    

class JsonFormatError(Exception):
    """exception for unexpected json response key"""
    pass

class OutputFileError(Exception):
    """exception for specified output files not being json"""
    pass


