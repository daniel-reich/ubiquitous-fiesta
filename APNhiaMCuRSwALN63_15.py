
def almost_palindrome(txt):
    backwards = txt[: : - 1]
    error = 0
    
    for i in range(len(txt)):
        if txt[i] != backwards[i]:
            error += 1
    print(txt, backwards,error)
    return error == 2

