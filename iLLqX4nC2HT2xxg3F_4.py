
def deepest(lst):
    depth = []
    deep = 0
    string = str(lst)
    for i in string:
        if i == '[':
            deep += 1
        elif i == ']':
            deep -= 1
        depth.append(deep)
    return max(depth)

