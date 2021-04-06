
def fibonacci(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    elif num==2:
        return 2
    else:
        return fibonacci(num-1)+fibonacci(num-2)

