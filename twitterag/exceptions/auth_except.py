## Author created exceptions go here##

class Error(Exception):
    pass


class ShellArgError(Error):
    """exception for when a shell argument is not in scope"""
    pass

class ParamTypeError(Error):
    """exception for invalid parameter (config) variable types"""
    pass


