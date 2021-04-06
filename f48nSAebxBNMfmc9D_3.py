
def check(word, mask):
    if len(word) != len(mask):
        return False
    for i in range(len(word)):
        if mask[i] != '*' and mask[i] != word[i]:
            return False
    return True
    
def scrambled(words, mask):
    return sorted([word for word in words if check(word, mask)])

