
def join_digits(n):
    word = "1"
    if n == 1:
        return word
    for i in range(2,n+1):
        if len(str(i)) <2:
            word += "-" + str(i)
        else:
            word += "-" + str(i)[0] + "-" + str(i)[1]
    return word

