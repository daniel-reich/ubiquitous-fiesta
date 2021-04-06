
def vowel_links(txt):
    words = txt.lower().split()
    vowels = 'aeiouy'
    for index, word in enumerate(words[:-1]):
        if word[-1] in vowels:
            if words[index + 1][0]  in vowels:
                return True
​
    return False

