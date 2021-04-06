
def secret(a):
    b=a.split(".")
    c=" ".join(b[1:])
​
   
    return "<{} class='{}'></{}>".format(b[0],c,b[0])

