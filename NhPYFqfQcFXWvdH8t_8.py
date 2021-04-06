
def gcd(a,b):
    return gcd(b,a%b) if b else a
​
def mod_inv(num, den):
    if gcd(num, den) != 1: return False
    advance = den//num + 1
    step = advance * num - den
    loop, jump, back = step, 1, 0
    while loop != 1:
        loop += step
        jump += 1
        if loop > num:
            loop -= num
            back += 1
    return jump * advance - back

