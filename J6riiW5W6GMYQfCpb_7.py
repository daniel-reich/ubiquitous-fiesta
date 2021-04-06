
def expensive_orders(d, k):
    mydict={}
    for key,value in d.items():
        if value>k:
            mydict[key]=value
    return mydict

