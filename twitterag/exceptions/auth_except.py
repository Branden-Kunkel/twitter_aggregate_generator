## author exceptions ##

class InvalidArgument(Exception):
    """exception for when a shell argument is not in scope"""

    def __init__(self, shell_arg):

        self.shell_arg = shell_arg

    
    def error_message(self, arg):
        print("\nError: Invalid argument in " + str(arg) + "\n")
        
    pass

class InvalidParameterType(Exception):
    """exception for invalid parameter (config) variable types"""

    def __init__(self, parameter):

        self.parameter = parameter

    def error_message(self, parameter):
        print("\nError: Invalid parameter type in " + parameter + "\n")
        return


