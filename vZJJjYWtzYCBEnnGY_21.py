
def number(a):
    m = 0
    for x in a:
        if x[0] in ("3"):
            m += 10
        elif x[0] == "A":
            m += 11
        elif x[0] == "T":
            m += 10
        elif x[0] == "K":
            m += 4 
        elif x[0] == "Q":
            m += 3 
        elif x[0] == "J":
            m += 2
    return m
​
def briscola_score(a, b):
    n = 0
    m = 0
    
    n = number(a)
    print("You score %i points in the first round." %(n))
    print("You need to score at least %i points in the second round." %(120-n+1))
​
    m = number(b)
    print("You score %i points in the second round." %(m))
    if m + n > 120:
        return "You Win!"
    elif m + n < 120:
        return "You Lose!"
    elif m + n == 120:
        return "Draw!"

