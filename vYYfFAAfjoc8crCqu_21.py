
def tree(h):
    return [" "*(((h)*2-i)//2)+ "#"*i+ " "*(((h)*2-i)//2) for i in [(1+(i)*2) for i in range(h)]]

