
def palindrome_descendant(num):
    return descendant(str(num))
​
def descendant(rep):
    if len(rep) == 1:
        return False
    elif rep == rep[::-1]:
        return True
    else:
        desc = "".join([str(int(rep[2*i]) + int(rep[2*i + 1])) for i in range(int(len(rep)/2))])
        return descendant(desc)

