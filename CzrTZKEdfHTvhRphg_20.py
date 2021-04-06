
def pgcd(num1, num2):
    for val in range(min(num1, num2), 0, -1):
        if num2%val == 0 and num1%val == 0 : return val
​
def mixed_number(frac):
    up, down = list(map(lambda elm: int(elm), frac.split('/')))
    if up == 0: return '0'
    up = abs(up)
    div = pgcd(up, down)
    up, down = up//div, down//div
    
    num = up//down
    result = '-' if frac[0] == '-' else ''
    if num == up/down: return result + str(num)
    result += str(num)+' ' if num != 0 else ''
    result += str(up - num*down) + '/' + str(down) if num != up/down else str(num)
    
    return result

