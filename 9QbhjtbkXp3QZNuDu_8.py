
def generate_palindromes(limit):
    return [n for n in range(11,limit+1) if str(n)[::-1]==str(n)][-15:]

