
def resist(net):
    if isinstance(net, str):
        return resist(eval(net))
    elif isinstance(net, tuple):
        return round(sum(i if isinstance(i, int) or isinstance(i, float)
                     else resist(i) for i in net), 1)
    elif isinstance(net, list):
        return round(1 / sum(1 / i if isinstance(i, int)
                             or isinstance(i, float)
                     else 1 / resist(i) for i in net), 1)

