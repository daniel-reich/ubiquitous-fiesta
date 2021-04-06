
def loves_me(n):
    a = "Loves me" 
    b = "Loves me not"
    if n==1:
        return "LOVES ME"
    else:
        return ', '.join([a if i%2==0 else b for i in range(n-1)])+ ', ' +[a if i%2==0 else b for i in range(n)][-1].upper()

