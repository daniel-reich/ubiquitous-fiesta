
def letters(word1, word2):
​
    return [("".join(sorted(set(word1).intersection(set(word2))))), ("".join(sorted((set(word1).difference(set(word2)))))),("".join(sorted((set(word2).difference(set(word1))))))]

