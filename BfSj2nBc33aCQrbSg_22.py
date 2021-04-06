
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n%i == 0:
            return False
    return True
def truncatable(n):
    n_str = str(n)
    if '0' in n_str:
        return False
    
    length = len(n_str)
    left_flag = True
    for i in range(length):
        current_str = n_str[i:]
        current = int(current_str)
        if not is_prime(current):
            left_flag = False
            break
    
    right_flag = True
    for i in range(length):
        current_str = n_str[:i+1]
        current = int(current_str)
        if not is_prime(current):
            right_flag = False
            break
    if left_flag:
        if right_flag:
            return "both"
        else:
            return "left"
    elif right_flag:
        return "right"
    else:
        return False

