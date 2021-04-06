
def loves_me(n):
    c=""
    for i in range(1,n+1,1):
        if i==n:
            if i%2==0:
                c+="LOVES ME NOT"
            else:
                c+="LOVES ME"
        elif i%2!=0:
            c+="Loves me" + "," + " "
        elif i%2==0:
            c+="Loves me not" + "," + " "
    return c
r=loves_me(1)
print(r)

