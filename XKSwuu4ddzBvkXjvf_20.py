
from string import punctuation, ascii_lowercase
​
​
def len_check(iterable):
    return [len(elem) for elem in iterable]
​
​
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
​
​
def remove_punc(sentence):
    for c in sentence:
        if c in punctuation or c == ' ':
            sentence = sentence.replace(c, ' ')
    return sentence.lower().split()
​
​
def sentence_primeness(sentence):
    letter_vals = {letter: i for i, letter in enumerate(ascii_lowercase, start=1)}
    totals = 0
​
    for elem in remove_punc(sentence):
        if elem.isalpha():
            for ch in elem:
                totals += letter_vals[ch]
        else:
            nums = sum(int(x) for x in list(elem))
            totals += nums
​
    if is_prime(totals):
        return 'Prime Sentence'
​
    words = ''.join([c for c in sentence if c not in punctuation]).split()
    word_total = 0
    removals = 0
    while words:
        primed_word = words.pop(0)
        removals += 1
        for word in words:
            if word.isalpha():
                for ch in word:
                    word_total += letter_vals[ch.lower()]
            else:
                nums = sum(int(x) for x in list(word))
                word_total += nums
​
        if is_prime(word_total):
            return 'Almost Prime Sentence ' + '(' + primed_word + ')'
        else:
            word_total = 0
            words.append(primed_word)
        if removals > len(words):
            break
    return 'Composite Sentence'

