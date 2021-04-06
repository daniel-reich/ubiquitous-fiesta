
def can_put(txt, dim):
    words = txt.split(' ')
    num_words = len(words)
    max_word_length = 0
    for word in words:
        if len(word) > max_word_length: max_word_length = len(word)
        if len(word) > dim[1]: return False
​
    if len(txt) <= dim[1]:
        return True
​
    if max_word_length <= dim[1] and num_words <= dim[0]:
        return True
    if len(words[0]+words[1]+' ')> dim[1]:
        return False

