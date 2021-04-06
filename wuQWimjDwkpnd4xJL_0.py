
def balanced(lst):
    h1, h2 = sorted((lst[:len(lst)//2], lst[len(lst)//2:]), key=sum)
    return lst if sum(h1) == sum(h2) else h2*2

