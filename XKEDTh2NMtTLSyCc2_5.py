
def valid_credit_card(n):
    total = 0
    digits = [int(i) for i in str(n)[::-1]]
    check = digits.pop(0)
​
    for idx, i in enumerate(digits):
        if idx%2:
            total += i
        else:
            total += i*2 if i < 5 else i*2 - 9
    return (9*total)%10 == check

