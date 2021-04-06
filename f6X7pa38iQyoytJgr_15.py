
def calculate_word_weight(word):
    return sum([ord(letter) for letter in word if letter.isalnum()])
​
​
​
def increasing_word_weights(sentence):
    weights = [calculate_word_weight(i) for i in sentence.split()]
    return weights == sorted(weights)

