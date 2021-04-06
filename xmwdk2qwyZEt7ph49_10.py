
def flatten(alist):
    new = []
    for x in alist:
        if type(x) != list:
            new.append(x)
        else:
            new += flatten(x)
    return new
​
def get_length(alist):
    return len(flatten(alist))

