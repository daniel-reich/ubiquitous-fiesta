
def resist(net):
    net = eval(net)
    def helper(net):
        for i in range(len(net)):
            if not isinstance(net[i],int):
                curr = helper(net[i])
                istuple = isinstance(net,tuple)
                net = list(net)
                net[i] = curr
                net = tuple(net) if istuple else list(net)
        if isinstance(net,tuple):
            return float(sum(net))
        else:
            return 1/(sum(1/i for i in net))
    return round(helper(net),1)

