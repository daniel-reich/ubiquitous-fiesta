
def resist(network):  # eval for fun
    return round({
        int: lambda x: x,
        str: lambda x: resist(eval(x)),
        tuple: lambda x: sum(map(resist, x)),
        list: lambda x: 1/sum(1/resist(i) for i in x)
    }.get(type(network))(network), 1)

