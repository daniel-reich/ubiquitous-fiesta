
def harry(po):
    if po[0]==[]:return -1
    if len(po)==1:return po[0][0]
    top=sum(po[0])
    bottom=sum(po[-1])
    left=sum([po[i][0]for i in range(len(po))][:-1])
    right=sum([po[i][-1]for i in range(len(po))][:-1])
    return max(top+right,bottom+left)

