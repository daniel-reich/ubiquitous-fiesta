
def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fact(n-1)*n
​
def eval_factorial(lst):
    myans = 0
​
    for i in range(len(lst)):
        myans += fact(int(lst[i][:-1]))
​
    return myans

