
def bugger(num):
    count = 0
    while len(str(num)) > 1:
        num = str(num)
        new_num = 1
        for char in num:
            new_num *= int(char)
        num = new_num
        count += 1
    
    return count

