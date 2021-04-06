
def num_args(func):
    '''
    Returns a count of the number of arguments passed with function func
    '''
    import inspect
​
    sig = inspect.signature(func)
    for p in sig.parameters.values():
        if str(p).startswith('*'):  # come from the Func class
            return len([arg for arg in args if arg != ','])
    return len(sig.parameters.values())

