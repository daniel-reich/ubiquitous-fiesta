
def strong_password(passwd):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    length = len(passwd)
    digit_flag = 0
    lower_flag = 0
    upper_flag = 0
    special_flag = 0
    for e in passwd:
        if e in numbers:
            digit_flag = 1
        elif e in lower_case:
            lower_flag = 1
        elif e in upper_case:
            upper_flag = 1
        elif e in special_characters:
            special_flag = 1
    total_flags = digit_flag+lower_flag+upper_flag+special_flag
    more_flags = 4 -total_flags
    if more_flags + length >=6:
        num_char_needed = more_flags
    else:
        num_char_needed = more_flags + (6 - (more_flags + length))
    
    return num_char_needed

