
def to_boolean_list(word):
    return list(map(lambda x:not((ord(x)-96)%2==0),list(word)))

