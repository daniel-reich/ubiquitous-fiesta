
# https://edabit.com/challenge/PCtTk9RRPPKXCxnAx
​
def modulo(a,b):
    if b < 0 and a > 0:
        return modulo(abs(a),abs(b))
    elif a<0 and b >0 :
        return -modulo(abs(a),abs(b))
    elif b > a and b >0 and a>0:
        return modulo(b, b-a)
    elif abs(a -b) < abs(b):
        return a-b
    return modulo((a-b),b)

