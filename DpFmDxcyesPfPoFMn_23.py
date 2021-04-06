
def isbn13(txt):
    if len(txt) == 10:
        if not divisible_by_eleven(multiply_isbn10(txt)):
            return 'Invalid'
        else:
            txt = '978' + txt
            txt = txt[:-1] + '0'
            while not divisible_by_ten(multiply_isbn13(txt)):
                txt = str(int(txt)+1)
            return txt
    elif len(txt) == 13:
        if divisible_by_ten(multiply_isbn13(txt)):
            return 'Valid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'
​
def multiply_isbn10(number):
    total = 0
    number = str(number)
    for count, num in enumerate(number):
        if num == 'x' or num == 'X':
            num = 10
        total += int(num) * isbn_10_keys[count+1]
    return total
​
def multiply_isbn13(number):
    total = 0
    number = str(number)
    for count, num in enumerate(number):
        total += int(num) * isbn_13_keys[count+1]
    return total
​
def divisible_by_ten(number):
    if int(number) % 10 == 0:
        return True
    return False
​
def divisible_by_eleven(number):
    if int(number) % 11 == 0:
        return True
    return False
​
isbn_10_keys = {1:10, 2:9, 3:8, 4:7, 5:6, 6:5, 7:4, 8:3, 9:2, 10:1}
isbn_13_keys = {1:1, 2:3, 3:1, 4:3, 5:1, 6:3, 7:1, 8:3, 9:1, 10:3, 11:1, 12:3, 13:1}
​
print(isbn13('031606652X'))

