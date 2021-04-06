
def bitwise_index(lst):
    x=([i for i in lst if i%2==0])
    if len(x)==0:
        return "No even integer found!"
    b=max(x)
    z=lst.index(b)
    if z%2==1:
        a="@odd index"+" "+str(z)
    else:
        a="@even index"+" "+str(z)
    y=([(str(a),b)])
    return dict(y)

