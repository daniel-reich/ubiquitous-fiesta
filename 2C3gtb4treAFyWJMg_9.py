
def polybius(text):
    t=text.split()
    ans=''
    alf='abcdefghiklmnopqrstuvwxyz'
    for i in range(len(t)):
        if t[0].isdigit():
            for j in range(0,len(t[i])-1,2):
                row=(int(t[i][j])-1)*5
                col=int(t[i][j+1])
                ans+=alf[row+col-1]
        else:
            for j in range(len(t[i])):
                p=alf.find(t[i][j].lower())
                if t[i][j].lower()=='j':p=8
                if p!=-1:
                    row=p//5+1
                    col=p%5+1
                    ans+=str(row)+str(col)             
        ans+=' '
    return ans[:-1]

