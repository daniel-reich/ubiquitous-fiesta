
def generate_palindromes(l):
    return [n for n in range(11, l+1) if n > 10 and str(n)[::-1] == str(n)][-15:]

