
def letters(word1, word2):
    shared = sorted([l for l in set(word1 + word2) if l in word1 and l in word2])
    w1_unique = sorted([l for l in set(word1) if l not in shared])
    w2_unique = sorted([l for l in set(word2) if l not in shared])
    return ["".join(shared), "".join(w1_unique), "".join(w2_unique)]

