
def babbage(n):
    x=int(n**.5)
    while x <= 269696:  
        if str(x**2)[-len(str(n)):]==str(n):
                if n==269696 and x==99736: return "Babbage was correct!"
                if n==269696 and x!=99736:return "Babbage was incorrect!"
                return x
        x+=1

