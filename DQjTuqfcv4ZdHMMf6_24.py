
def helper(n):
    digits = [c for c in str(n).zfill(4)]
    a = int(''.join(sorted(digits)))
    b = int(''.join(sorted(digits, reverse=True)))
    return b - a
    
def kaprekar(num): 
    cnt = 0
    while num != 6174:
        cnt += 1
        num = helper(num)
    return cnt

