
def happy(n):
    n=str(n)
    newn=0
    count=0
    while n != str(1):
​
        for number in n:
            newn=newn+int(number)**2
​
            n=str(newn)
​
​
​
        newn=0
        count=count+1
​
        if count > 10:
            return False
        print(n)
​
    return True

