
import string
import math
​
def tokenizer(s):
    lst = s.split()
    words = []
    for i in lst:
        words.append(i)
​
    wordJoin = " ".join(words)
    wordJoin = wordJoin.translate(str.maketrans({key: " {0} ".format(key) for key in string.punctuation}))
​
    return wordJoin
​
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
​
    sqr = int(math.sqrt(n)) + 1
​
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
​
def get_sums(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0
    num_sum = 0
    for i in s.lower():
        if i in alphabet:
            sum += alphabet.index(i) + 1
        if i.isdigit():
            num_sum += int(i)
    return sum + num_sum
​
def sentence_primeness(sentence):
    sent = tokenizer(sentence)
    splitter = sent.split()
    words = [w for w in splitter if w not in string.punctuation]
    i = 0
    dict = {}
    sum = 0
    while i < len(words):
        dict[words[i]] = get_sums(words[i])
        sum += get_sums(words[i])
        i += 1
​
    if is_prime(sum):
        return "Prime Sentence"
    else:
        for k,v in dict.items():
            v = sum-v
            if(is_prime(v)):
                return "Almost Prime Sentence (" + k + ")"
    return "Composite Sentence"

