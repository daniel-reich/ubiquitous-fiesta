
def fizz_buzz(maximum):
    l = list(range(1,maximum+1))
    li=[]
    for i in l:
        if i % 5 == 0 and i % 3 == 0:
            li.append("FizzBuzz")
        elif i % 5 == 0:
            li.append("Buzz")
        elif i % 3 == 0:
            li.append("Fizz")
        else:
            li.append(i)
    return li

