
def maximum_seating(lst):
    w=''.join([str(i) for i in lst]).split('1')
    if w[0]=='' and  w[-1]=='':
        return sum([(len(i)-2)//3 for i in w[1:-1] if len(i)>2])
    elif w[0]=='':
        return sum([(len(i)-2)//3 for i in w[1:-1] if len(i)>2])+(len(w[-1])//3)
    elif w[-1]=='':
        return sum([(len(i)-2)//3 for i in w[1:-1] if len(i)>2])+(len(w[0])//3)
    else:
        if len(w)>=2:
            return sum([(len(i)-2)//3 for i in w[1:-1] if len(i)>2])+(len(w[0])//3)+(len(w[-1])//3)
        else:
            return (len(w[0])-1)//3 +1

