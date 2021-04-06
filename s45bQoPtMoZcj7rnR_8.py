
def closest_palindrome(num):
    i = 0
    while True:
        if str(num-i) == str(num-i)[::-1]:
            return num-i
        if str(num+i) == str(num+i)[::-1]:
            return num+i
        i += 1

