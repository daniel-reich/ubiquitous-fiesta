
def is_disarium(n):
    sum = 0
    digits_lst = []
    digit_dict = dict()
    for i in str(n):
        digits_lst.append(i.split())
    for j in range(len(digits_lst)):
        for k in range(len(digits_lst[j])):
            digit_dict[j + 1] = int(digits_lst[j][k])
    for key, value in digit_dict.items():
        sum += value ** key
    if sum == n :
        return True
    return False    
    
print(is_disarium(518))

