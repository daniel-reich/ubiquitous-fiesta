
def closest_palindrome(num):
    n = str(num)
    if set(str(num -1)) == {'9'}: return num -1
    return int(n[:(len(n))//2] + n[(len(n)-1)//2::-1])

