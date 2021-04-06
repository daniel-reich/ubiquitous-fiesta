
def super_digit(n, k):
    def recursive(n):
        num = str(n)
        if len(num) == 1: return int(num)
        else: return recursive(sum(int(i) for i in str(num)))
    num = int(str(n)*k)
    return recursive(num)

