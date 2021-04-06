
import re
def find_longest(sentence, words='', big='', size=0):
    if words == '':
        pattern = re.compile('[^A-Za-z0-9]+')
        sentence = re.sub(pattern,' ',sentence)
        sentence = sentence.lower()
        words = sentence.split(' ')
    if len(words) == 0:
        return big
    word = words.pop()
    if len(word) >= size:
        big = word
        size = len(word)
    return find_longest(sentence, words, big, size)

