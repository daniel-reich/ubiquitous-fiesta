
def count_palindromes(num1, num2):
    x = list(range(num1,num2+1))
    res = 0
    for i in x:
        if i < 10:
            res +=1
        elif i > 10:
            i = str(i)
            if i == i[::-1]:
                res +=1
    return res

