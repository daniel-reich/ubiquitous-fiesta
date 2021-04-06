
def fibonacci_sequence():
    lst=[0,1]
    i=0
    while lst[i+1]<255:
        lst.append(lst[i]+lst[i+1])
        i +=1
    lst.remove(lst[-1])
    return lst

