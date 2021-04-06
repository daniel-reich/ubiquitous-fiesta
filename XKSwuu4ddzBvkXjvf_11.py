
import string
def sentence_primeness(sentence):
    cleaned_sent = sentence.translate(sentence.maketrans('', '', string.punctuation))
    words = cleaned_sent.split()
    print(words)
    return sentence_primeness_helper(words)
​
def sentence_primeness_helper(word_lst):
    sent_val = sentence_value(word_lst)
    if is_prime(sent_val):
        return "Prime Sentence"
    for word in word_lst:
        print(word)
        new_word_lst = list(word_lst)
        new_word_lst.remove(word)
        if is_prime(sentence_value(new_word_lst)):
            return "Almost Prime Sentence " + "(" + word + ")"
    return "Composite Sentence"
​
def sentence_value(word_lst):
    return sum([char_value(char) for word in word_lst for char in word])
​
def char_value(char):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if char.lower() in alphabet:
        return alphabet.index(char.lower()) + 1
    return int(char) # char is a numerical character
​
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

