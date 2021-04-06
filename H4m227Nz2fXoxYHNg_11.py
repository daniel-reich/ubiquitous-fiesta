
def list_values_types(lst):
    d = {type(True):'bool',
         type(22):'int',
         type(2.1):'float',
         type('abc'):'str',
         type([1]):'list',
         type({}): 'dict',
         type(None):'NoneType'}
    return [(d[type(x)]) for x in lst]

