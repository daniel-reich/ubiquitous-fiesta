
def factory(n):
    def f(lst):
        return [v // n for v in lst]
    return f

