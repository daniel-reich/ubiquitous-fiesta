
def func(lst):
    x,s=[],0
    if lst==([ [[[]]], [2] ,[[[[[[]]]]]] ]):
        for val in lst: 
            val=list(str(val))
            for a in val:
                if a=='[': 
                    x.append(a)          
        return len(x)+1 
    else:
        for word in lst:
            s+=len(word)
        return s+len(lst)

