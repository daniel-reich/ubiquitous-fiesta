
def lazy(lst):
    for i in lst:
        if type(i) is list:
            yield int(str(i)[1:-1]), i
        else:
            yield i, i
 
​
sort_it=lambda z: [y for _, y in sorted(lazy(z))]

