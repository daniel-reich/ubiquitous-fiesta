
def double_letters(str1):
    for i in range(len(str1)-1):
        if str1[i] == str1[i+1]:
            return True
    return False

