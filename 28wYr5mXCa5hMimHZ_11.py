
def valid_name(name):
    letters = []
    dot = 0
    for x in name:
        letters.append(x)
    count = 0
    for x in letters:
        if x == " ":
            count += 1
​
    print(count)
    if count == 0:
        return False
    if count > 2:
        return False
​
    first = 0
    second = 0
    third = 0
    for x in letters:
        print(x)
        if not(x == " "):
            first += 1
        else:
            break
    for x in letters[first+1:]:
​
        if not(x == " "):
            second += 1
        else:
            break
    for x in letters[first+second+2:]:
        third += 1
​
    print(first)
    print(second)
    print(third)
​
    if third < 3 and not(second > 0):
​
        return False
​
    if third == 0 and second < 3:
        return False
​
    if first < 3 and second >= 3 and not(third == 0):
        return  False
​
    if second == 0:
        return False
​
    if first == 1:
        return  False
​
    if second == 1:
        return False
​
    if third == 1:
        return False
​
    if str.isupper(letters[0]) == False:
        return False
    if str.isupper(letters[first + 1]) == False:
        return False
    if not(third==0):
        if str.isupper(letters[first+second+2]) == False:
            return False
​
​
    if not (third == 0):
        if first < 3 and second > 2:
            return False
    if letters[first-1] == "." and not (first == 2):
        return False
    if letters[first + second] == "." and not(second == 2):
        return False
    if letters[-1] == ".":
        return False
​
    return True

