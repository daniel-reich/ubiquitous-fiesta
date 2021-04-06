
def count_same_ends(txt):
    words = ''.join([c if c.isalpha() else ' ' for c in txt.lower()]).split()
    return sum([len(word) > 1 and word[0] == word[-1] for word in words])

