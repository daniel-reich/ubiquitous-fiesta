
def is_kaprekar(n):
    s = str(n**2).zfill(2)
    return int(s[:len(s)//2]) + int(s[len(s)//2:]) == n
​
def kaprekar_numbers(p, q):
    nums = [str(i) for i in range(p, q + 1) if is_kaprekar(i)]
    return ' '.join(nums) or "INVALID RANGE"

