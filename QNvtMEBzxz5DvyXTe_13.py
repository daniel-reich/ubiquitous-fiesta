
def strong_password(password):
    special = '!@#$%^&*()-+'
    digit_in, upper_in, lower_in, special_in = 1, 1, 1, 1
    for c in password:
        if c.isdigit():
            digit_in = 0
        elif c.isalpha():
            if c.islower():
                lower_in = 0
            elif c.isupper():
                upper_in = 0
        elif c in special:
            special_in = 0
    add_on = digit_in + upper_in + lower_in + special_in
    return add_on if add_on + len(password) > 5 else 6 - len(password)

