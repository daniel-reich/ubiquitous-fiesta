
def valid_credit_card(number):
    s = str(number)
    sum1 = sum([f(s[i]) for i in range(len(s)-2,-1,-2)])
    sum2 = sum([int(s[i]) for i in range(len(s)-3,-1,-2)])
    return 9 * (sum1 + sum2) % 10 == int(s[-1])
          
def f(s):
    x = 2*int(s)
    if x > 9:
        x = x-9
    return x

