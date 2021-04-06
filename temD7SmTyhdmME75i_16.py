
def to_boolean_list(word):
    myans = []
    for i in word:
        myans.append(bool((ord(i))%2))
    return myans

