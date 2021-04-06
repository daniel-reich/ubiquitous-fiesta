
def score_it(string):
    total, count_parentheses, found_num = 0, 0, True
    num_so_far = ""
    for char in string:
        if char == "(": 
            if found_num and num_so_far:
                found_num = False
                total += int(num_so_far) * count_parentheses
                num_so_far = ""
            count_parentheses += 1
        elif char == ")":
            if found_num and num_so_far:
                found_num = False
                total += int(num_so_far) * count_parentheses
                num_so_far = ""
            count_parentheses -= 1
        elif char.isdigit(): 
            num_so_far += char
            found_num = True
    return total

