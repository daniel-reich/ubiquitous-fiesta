
def can_complete(initial, word):
    index = 0
    for ele in initial:
        if ele not in word:
            return False
        else:
            index = word.index(ele)
            word = word[index+1::]
    return True

