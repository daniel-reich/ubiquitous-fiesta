
def shared_letters(str1, str2):
    return sum(i in set(str2) for i in set(str1))

