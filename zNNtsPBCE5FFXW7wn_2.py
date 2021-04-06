
def empty_values(lst):
    d = {type(1):0,
         type(1.0):0.0,
         type('a'):'',
         type(True):False,
         type([1]):[],
         type((1,)):(),
         type({1}):set(),
         type(None):None,}
    return [d[type(x)] for x in lst]

