
def fibonacci(num):
    if num == 0:
        return 1
    else:
        return round((((1.618034)**(num+1))-((0.618034)**(num+1)))/(5**0.5))

