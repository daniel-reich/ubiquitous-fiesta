
def eval_resist(net):
    if isinstance(net, list):
        #parallel
        return 1 / sum(1 / eval_resist(rn) for rn in net)
    elif isinstance(net, tuple):
        #series
        return sum(eval_resist(rn) for rn in net)
    else:
        #value
        return net
​
def resist(net):
    return round(eval_resist(eval(net)), 1)

