
def is_zygodrome(num):
    num = str(num)
    if len(num) == 1:
        return False
    while len(set(num)) > 1:
        for i in range(1, len(num)):
            if num[i] != num[i - 1]:
                num = num[i : ]
                if i == 1 or len(num) == 1:
                    return False
                else:
                    break
    return True

