
def fizz_buzz(maximum):
    
    res = [0]
    for i in range(1, maximum+1):
        res.append(i)
        if i % 15 == 0:
            res[i]= "FizzBuzz"
        elif i % 3 == 0:
            res[i]= "Fizz"    
        elif i % 5 == 0:
            res[i]= "Buzz"
    res.pop(0)
    return res

