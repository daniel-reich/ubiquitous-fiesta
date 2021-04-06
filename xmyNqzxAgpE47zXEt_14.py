
def check_word(word):
    word = [c for c in word.lower() if 'a' <= c <= 'z']
    if len(word) < 3:
        return False
    return all([word[i] >= word[i-1] for i in range(1, len(word))])
​
def is_alphabetically_sorted(sentence):
    return any([check_word(word) for word in sentence.split()])

