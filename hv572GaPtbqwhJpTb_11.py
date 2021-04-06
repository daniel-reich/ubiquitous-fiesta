
def elasticize(word):
    if len(word)%2==0:
        n=len(word)//2
        x=[(i+1)*word[i] for i in range(n)]
        y=[(n-i)*word[n:][i] for i in range(n)]
        return ''.join(x+y)
    else:
        n=len(word)//2
        x=[(i+1)*word[i] for i in range(n)]
        y=[(n-i)*word[n+1:][i] for i in range(n)]
        return ''.join(x+[word[n]*(n+1)]+y)

