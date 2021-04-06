
def fibonacci_sequence():
    lst = [0,1]
    while lst[-1]<230:
        lst.append(lst[-1]+lst[-2])
    return lst

