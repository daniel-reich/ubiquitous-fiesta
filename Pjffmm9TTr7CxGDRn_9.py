
def is_ascending(num_str, num_len=1):
    if num_len > len(num_str)//2:
        return False
    if check_ascending(num_str, num_len):
        return True
    return is_ascending(num_str, num_len+1)
​
def check_ascending(num_str, num_len):
    if len(num_str) <= num_len:
        return True
    current_num = int(num_str[:num_len])
    next_num = int(num_str[num_len:(num_len+num_len)])
    if current_num + 1 == next_num:   
        return check_ascending(num_str[num_len:],num_len)
    else:
        return False

