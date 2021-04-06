
def str_to_dict(lst):
    mylst= list()
    mydict= dict()
    for i in lst:
        c=i.split("=")
        mylst.append(c)
    for i in mylst:
        mydict[i[0]]=i[1]  
    return mydict

