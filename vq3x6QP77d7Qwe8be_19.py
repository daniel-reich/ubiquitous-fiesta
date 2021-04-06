
def odd_square_patch(lst):
    count=0
    x,y=[],[]
    for word in lst:
        for i in word:
            if i%2==1:
                count+=1
        x.append(count)
        if count<=2:
            y.append(word)
        count=0
    if x[0]==0:
        return x[0]
    if len(lst)==1or (len(lst)==3 and lst[1]==y[0])or (len(lst)==1 and min(x)==2):
        return 1 
    else:
        return min(x)

