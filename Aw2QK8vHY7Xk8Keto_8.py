
def longest_word(sentence):
    words = sentence.split()
    lengths = [len(word) for word in words]
    longest = max(lengths)
​
    for word in words[::-1]:
        if len(word) == longest:
            longest_word = word
​
    return longest_word

