
def factory(n):
    def mk_lst(lst):
        return [int(i/n) for i in lst]
    return mk_lst

