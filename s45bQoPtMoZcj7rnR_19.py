
def closest_palindrome(n):
    it = 0
    while(True):
        if n - it == int(str(n-it)[::-1]):return n-it
        if n + it == int(str(n+it)[::-1]):return n+it
        it+=1

