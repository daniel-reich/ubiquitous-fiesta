
def can_build(s1, s2):
    list1, list2 = [letter for letter in s1], [letter for letter in s2]
    for letter in list2:
        if letter in list1:
            list1.remove(letter)
        else:
            return False
    return True

