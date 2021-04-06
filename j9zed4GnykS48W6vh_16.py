
def digits(number):
​
    lst_1, lst_2 = [], []
​
    for i in range(len(str(number))):
        lst_1.append(int('1' + '0' * (i)))
​
    calc_1 = (number - lst_1[-1])*(len(str(number)))
​
    for i in range(len(lst_1) - 1):
        lst_2.append((lst_1[i + 1] - lst_1[i])*(len(str(lst_1[i]))))
​
    lst_2.append(calc_1)
​
    return sum(lst_2)

