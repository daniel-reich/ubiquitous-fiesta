
def generate_palindromes(limit):
    a=[]
    for i in range(limit+1):
        if str(i)==str(i)[::-1]:
            a.append(i)
    return a[-15:]

