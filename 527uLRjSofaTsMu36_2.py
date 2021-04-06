
def get_middle(word): 
    m = (len(word) - 1) // 2
    l = 1 if len(word) % 2 else 2
    return word[m:m+l]

