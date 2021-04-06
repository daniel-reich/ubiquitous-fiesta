
def peel_layer_off(lst):
    return list(map(lambda x:x[1:len(x)-1], lst[1:len(lst)-1]))

