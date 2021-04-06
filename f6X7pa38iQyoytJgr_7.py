
def increasing_word_weights(s):
    s = ''.join(i for i in s if i.isalpha() or i == ' ')
    weights = [sum(ord(i) for i in word) for word in s.split()]
    return weights == sorted(weights) and len(weights) == len(set(weights))

