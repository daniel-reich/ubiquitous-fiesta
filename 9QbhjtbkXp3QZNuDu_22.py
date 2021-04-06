
def generate_palindromes(limit):
    palindrome = []
    for num in range(11, limit + 1):
        if str(num)[::-1] == str(num):
            palindrome.append(num)
    return palindrome[-15:]

