
def find_simple_structure(net, open_symbol, close_symbol):
    closing = [i for i in range(len(net)) if net[i] == close_symbol]
    for end in closing:
        start = end - 1
        while start >= 0 and (net[start] == ',' or type(net[start]) == float or net[start] == open_symbol):
            if net[start] == open_symbol:
                return start, end
            start -= 1            
    return -1, -1
​
def replace_simple_series(net, start, end):
    replace_res = sum([float(res) for res in net[start+1:end:2]])
    net[start] = replace_res
    net = net[:start+1] + net[end+1:]
    return net
​
def replace_simple_parallel(net, start, end):
    replace_res = 1. / sum([1. / float(res) for res in net[start+1:end:2]])
    net[start] = replace_res
    net = net[:start+1] + net[end+1:]
    return net
        
def resist(net):
    for symbol in "()[],":
        net = net.replace(symbol, ' ' + symbol + ' ')
    net = net.split()
    for i in range(len(net)):
        try:
            net[i] = float(net[i])
        except:
            pass
    while True:
        start, end = find_simple_structure(net, '(', ')')
        if start >= 0:
            net = replace_simple_series(net, start, end)
        start, end = find_simple_structure(net, '[', ']')
        if start >= 0:
            net = replace_simple_parallel(net, start, end)
        if len(net) == 1:
            ans = round(float(net[0]), 1)
            return ans

