
def is_palindrome_possible(txt):
    j = 0
    char_list = []
    duplicate_count = 0
​
    for i in range(len(txt)):
        char_list.append(txt[i])
    char_list = sorted(char_list)
    while j < len(char_list) - 1:
        if char_list[j] == char_list[j+1]:
            duplicate_count += 1
            j += 2
        else:
            j += 1
    if len(txt) % 2 == 0 and len(txt) - (duplicate_count*2) == 0:
        return True
        # even
    elif len(txt) % 2 == 1 and len(txt) - (duplicate_count*2) == 1:
        return True
        # odd
    else:
        return False

