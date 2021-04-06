
def is_heteromecic(n):
    def recursive(n, cnt):
        prd = cnt*(cnt+1)
        if prd == n: return True
        elif cnt > n: return False
        else: return recursive(n, cnt+1)
    if n == 0: return True
    else: return recursive(n, 1)

