
def fibonacci_sequence():
    res = [0,1]
    while(res[-1]<255):
        res.append(res[-1]+res[-2])
    return res[:len(res)-1]

