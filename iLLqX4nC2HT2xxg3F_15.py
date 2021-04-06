
def deepest(lst):
    caves = []
    deep = 0
    string = str(lst)
    for i in string:
        if i == '[':
            deep += 1
        elif i == ']':
            deep -= 1
        caves.append(deep)
    return max(caves)

