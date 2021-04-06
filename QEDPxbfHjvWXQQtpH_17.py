
def count_palindromes(num1, num2):
    return sum(str(i) == str(i)[::-1] for i in range(num1, num2 + 1))

