
# without regex
def strong_password(password):
    up = low = digit = special = False
​
    for letter in password:
        if letter.isupper():
            up = True
        elif letter.islower():
            low = True
        elif letter.isdigit():
            digit = True
        elif letter in "!@#$%^&*()-+":
            special = True
​
    missing_criteria = 4 - sum((up, low, digit, special))
    new_size = len(password) + missing_criteria
​
    if new_size >= 6:
        return missing_criteria
    return 6 - new_size + missing_criteria

