
def is_kaprekar(n):
    if len(str(n))==1 :
        if n==9 or n==1:
            return True
        else:
            return False
    else:
​
        x=str(n*n)
        if int(x) % 2 == 0 and int(x[:len(x) // 2]) + int(x[len(x) // 2:]) == n:
            return True
        elif int(x)%2!=0 and int(x[:len(x) // 2]) + int(x[len(x) // 2:]) == n:
            return True
        else:
            return False

