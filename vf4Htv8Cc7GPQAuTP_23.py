
def list_operation(x, y, n):
​
    number_list = [ e for e in range(x,y+1) if e % n == 0]
    return number_list

