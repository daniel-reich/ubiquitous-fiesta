
def bitwise_index(lst):
    mx=0
    for i in lst:
        if i%2==0 and i>mx:
            mx=i
        else:
            mx=mx
    if mx not in lst:
        return "No even integer found!"
    elif lst.index(mx)%2==0:
        return {"@even index "+str(lst.index(mx)) : mx}
    else:
        return {"@odd index "+str(lst.index(mx)) : mx}

