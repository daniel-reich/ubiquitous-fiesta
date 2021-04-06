
def bugger(n):
    count = 0
    while True:
        valors = number_operations(n)
        if valors[1] == 1:
            return count
        n = valors[0]
        count += 1
​
​
def number_operations(n):
    digits = list(str(n))
    valor = 1
    for num in digits:
        valor *= int(num)
    return [valor, len(digits)]

