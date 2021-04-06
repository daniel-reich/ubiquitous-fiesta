
def possible_palindrome(txt):
    lst = []
    for item in set(txt):
        lst.append(txt.count(item))
    neg = False
    for num in lst:
        if len(txt)%2 == 0 and num%2 != 0 or num%2 != 0 and neg == True:
            return False
        elif num%2 != 0:
            neg = True
    return True

