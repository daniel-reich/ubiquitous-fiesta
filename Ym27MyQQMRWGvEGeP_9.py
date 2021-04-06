
def is_consecutive(num_str, num_len=1):
    if num_len > len(num_str)//2:
        return False
    up, down = True, True
    if check_consecutive(num_str, num_len, up, down):
        return True
    return is_consecutive(num_str, num_len+1)
​
def check_consecutive(num_str, num_len, up, down):
    if len(num_str) <= num_len:
        return True
    current_num = int(num_str[:num_len])
    next_num = int(num_str[num_len:(num_len+num_len)])
    if (current_num + 1 == next_num) and up:
        down = False
        return check_consecutive(num_str[num_len:],num_len, up, down)
    elif (current_num - 1 == next_num) and down: 
        up = False  
        return check_consecutive(num_str[num_len:],num_len, up, down)
    else:
        return False

