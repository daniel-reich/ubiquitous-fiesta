
def make_plus_function(base_num):
    def inner_func(newarg):
        return newarg + base_num
    return inner_func

