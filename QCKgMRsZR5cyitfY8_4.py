
def get_type(value):
    if type(value) is int:
        return 'int'
    elif type(value) is float:
        return 'float'
    elif type(value) is bool:
        return 'bool'
    elif type(value) == type(None):
        return 'NoneType'
    elif type(value) is list:
        return 'list'
    elif type(value) is str:
        return 'str'
    elif type(value) is set:
        return 'set'
    elif type(value) is tuple:
        return 'tuple'
    elif type(value) is dict:
        return 'dict'

