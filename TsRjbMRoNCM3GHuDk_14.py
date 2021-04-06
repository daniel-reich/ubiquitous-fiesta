
vowels = "aAeiou"
​
def syllabification(word):
    ind = [i for i in range(len(word)) if word[i] in vowels]
    if len(ind) == 1:
        return word
    blocks = []
    i1 = ind[0]
    for i2 in ind[1:]:
        blocks.append(word[i1 - 1:i2 - 1])
        i1 = i2
    blocks.append(word[i1 - 1:])
    return '.'.join(blocks)

