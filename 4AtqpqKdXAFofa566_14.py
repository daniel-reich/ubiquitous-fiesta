
def remove_leading_trailing(num: str) -> str:
    if len(set(num)) == 1 and '0' in num:
        return '0'
    elif len(set(num)) == 2 and '0' in num and '.' in num:
        return '0'
    temp = list(num)
    if '.' in num:
        for i in range(len(num) - 1, num.index('.') - 1, -1):
            if num[i] == '0' or num[i] == '.':
                temp.pop()
            else:
                break
    while temp[0] == '0':
        if temp[1] == '.':
            break
        temp.pop(0)
    return ''.join(temp)

