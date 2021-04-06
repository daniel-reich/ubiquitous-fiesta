
def shift_sentence(txt):
    words = txt.split()
    c_last = words[-1][0]
    word2 = words[-1]
    for i in range(len(words) - 2, -1, -1):
        word1 = words[i]
        word2 = word1[0] + word2[1:]
        words[i+1] = word2
        word2 = word1
    words[0] = c_last + words[0][1:]
    return ' '.join(words)

