
OP = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__, '/':int.__floordiv__}
def prefix(exp):
    def calc():
        i = items.pop(0)
        return OP[i](calc(), calc()) if i in OP else int(i)
    items = exp.split()
    return calc()

