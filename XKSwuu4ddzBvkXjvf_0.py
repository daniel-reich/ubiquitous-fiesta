
import re
​
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True
​
def word_value(word):
    total = 0
    for i in word.lower():
        if i.isnumeric():
            total += int(i)
        elif i.isalpha():
            total += ord(i) - 96
    return total
​
def sentence_primeness(sentence):
    sentence = re.sub(r'[^\w ]', '', sentence).split()
    values = [(word_value(word), word) for word in sentence]
    total = sum(value for value, word in values)
​
    if is_prime(total):
        return 'Prime Sentence'
    for value, word in values:
        if is_prime(total - value):
            return 'Almost Prime Sentence ({})'.format(word)
    return 'Composite Sentence'

