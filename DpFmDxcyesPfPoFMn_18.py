
def is_isbn10(num):
    return (11-(sum((10 - i) * int(num[i]) for i in range(len(num)-1)) % 11)) % 11 == 10 if num[-1] == "X" else 11 - sum((10 - i) * int(num[i]) for i in range(len(num)-1)) % 11 == int(num[-1])
​
​
def check_digit(num):
    check = 10 - sum(1 * int(num[i]) if i % 2 == 0 else 3 *
                     int(num[i]) for i in range(len(num)-1)) % 10
    return check if 0 <= check < 10 else ""
​
​
def is_isbn13(num):
    return 10 - sum(1 * int(num[i]) if i % 2 == 0 else 3 * int(num[i]) for i in range(len(num)-1)) % 10 == int(num[-1])
​
​
def isbn13(txt):
    if len(txt) == 13:
        return "Valid" if is_isbn13(txt) else "Invalid"
    if is_isbn10(txt):
        check = check_digit("978" + txt)
        if check != "":
            if is_isbn13("978" + txt[:-1] + str(check)):
                return "978" + txt[:-1] + str(check)
    return "Invalid"

