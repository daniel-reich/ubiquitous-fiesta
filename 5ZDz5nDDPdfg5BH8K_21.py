
def only_5_and_3(n):
    a = 0
    three = []
    
    for i in range(0, n + 1):
        
        if i % 3 == 0 and i % 2 != 0:
                                       
            three.append(i)
    three_mul = [0,3]        
    for i in three:
        if i ** 1/3 in three:
            three_mul.append(i)
​
    print(three)        
    print(three_mul)
    five = []
    for i in range(0, n + 1):
        if i % 5 == 0:
            five.append(i)
        
​
    for i in three_mul:
        for j in five:
            if i + j == n:
                print(i,j)
                a = 1
    if a == 1:
        return True
    else:
        return False

