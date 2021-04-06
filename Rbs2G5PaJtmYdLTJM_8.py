
def is_heteromecic(n):
    if n == 0: return True
    cnt = 1; prd = 1
    while cnt < n:
        prd = cnt*(cnt+1)
        if prd == n: return True
        cnt += 1
    else: return False

