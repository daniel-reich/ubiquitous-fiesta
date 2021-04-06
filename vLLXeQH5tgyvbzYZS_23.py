
def is_prim_pyth_triple(numbers):
    numbers.sort()
    if is_rectangle(numbers):
        
        dividers = {}
        for element in numbers:
            aux = []
            for i in range(2,element):
                if element%i == 0:
                    aux.append(i)
            dividers[element] = aux
​
        for i in range(2):
            for element in dividers[numbers[i]]:
                if element in dividers[numbers[i+1]]:
                    return False
        return True
​
    else:
        return False
​
def is_rectangle(numbers):
    if numbers[0]**2+numbers[1]**2 == numbers[2]**2:
        return True
    return False

