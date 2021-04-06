
letters = {"H", "I", "N", "O", "S", "X", "Z", "W"}
def rotated_words(txt):
    return len(set(w for w in txt.split() if all(c in letters for c in w)))

