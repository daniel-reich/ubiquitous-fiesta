
def cards_needed(n1):
    return(sum([i for i in range(1,n1+1)])+n1**2 if n1>=0 else "invalid")

