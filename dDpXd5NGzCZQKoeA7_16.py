
def num_args(func):
    try:
        eval('func()')
    except TypeError as err:
        beg = 8 + str(err).index('missing')
        end = -1 + str(err).index('required')
        return int(str(err)[beg:end])        
    return 0

