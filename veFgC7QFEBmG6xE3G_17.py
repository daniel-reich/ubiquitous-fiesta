
def is_smooth(sentence):
​
    words = sentence.split()
​
    first_word = True
​
    for word in words:
​
        if first_word:
            last = word[-1].lower()
            first_word = False
            continue
​
        first = word[0].lower()
​
        if first != last:
            return False
​
        last = word[-1]
​
    return True

