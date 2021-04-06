
def is_sorted(words, alphabet):
    translation = {alphabet[i]: chr(97+i) for i in range(26)}
    words = [''.join([translation[c] for c in word]) for word in words]
    return words == sorted(words)

