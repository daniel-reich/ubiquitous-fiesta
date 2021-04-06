
def count_palindromes(num1, num2):
    lst = [x for x in range(num1, num2 + 1)]
    n = 0
    for i in lst:
        if str(i) == str(i)[::-1]:
            n += 1
        n += 0
    return n

