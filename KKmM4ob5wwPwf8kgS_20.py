
def get_frequencies(lst):
    a = sorted(set(lst),reverse=False)
    new=[]
    for i in a:
        b = lst.count(i)
        new.append(b)
    data=dict(zip(a,new))
    return data
​
print(get_frequencies([1,2,3,3,2]))

