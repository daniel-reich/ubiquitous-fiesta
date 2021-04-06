
def shift_sentence(txt):
    words = txt.split()
    firsts, others = [], []
​
    for word in words:
        firsts.append(word[0])
        others.append(word[1::])
​
    shifted_words = [firsts[i - 1] + others[i] for i in range(len(words))]
    shifted_sentence = ' '.join(shifted_words)
​
    return shifted_sentence

