
def bitwise_index(lst):
    max=-1
    index=0
    dict={}
    for i,x in enumerate(lst):
        if x%2==0:
            if max<x:
                max=x
                index=i
    if index%2==0:
        parity="even"
    else:
        parity="odd"
    if max==-1 and index==0:
        return "No even integer found!"
    else:
        dict["@{} index {}".format(parity,index)]=max
        return dict

