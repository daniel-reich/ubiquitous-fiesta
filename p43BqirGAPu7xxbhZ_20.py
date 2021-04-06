
def diamond(n):
    res=eval(str([[0]*n]*((n+1)//2)))
    col=0
    for row in range((1+n)//2):
        res[row][n//2+col]=1
        res[row][-col-n//2-1]=1
        col+=1
    return [res+res[-2::-1], 'perfect cut' if n%2 else 'good cut']

