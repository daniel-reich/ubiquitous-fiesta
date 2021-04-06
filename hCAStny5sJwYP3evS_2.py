
def is_early_bird(_range, n):
    l = len(str(n))
    cat = [k for k in range(nat_ind(_range+1)+l+1) if "".join(str(i) for i in range(_range+1))[k:k+l]==str(n)]
    return [list(range(k,k+l)) for k in cat] + ['Early Bird!']*(min(cat)!=nat_ind(n))
​
def nat_ind(n):
    l = len(str(n))
    return 9*sum(i*(10**(i-1)) for i in range(1,l)) + l*(n-10**(l-1))+1

