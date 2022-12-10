## Author created exceptions go here##

class Error(Exception):
    pass


class ShellArgError(Error):
    """exception for when a shell argument is not in scope"""
    pass

class ParamTypeError(Error):
    """exception for invalid parameter (config) variable types"""
    pass

class JsonFormatError(Error):
    """exception for unexpected json response key"""
    pass

class OutputFileError(Error):
    """exception for specified output file being something other than .json"""
    pass


