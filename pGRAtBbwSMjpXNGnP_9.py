
def is_sorted(words, alphabet):
    if words == []:
        return True
    for i in range(len(words)-1):
        min_len = min(len(words[i]), len(words[i+1]))
        if words[i+1] == words[i][0:min_len] and len(words[i]) > min_len:
                 return False
        for j in range(min_len):
            if all(words[i][k] == words[i+1][k] for k in range(j)) and alphabet.find(words[i][j]) > alphabet.find(words[i+1][j]):
                return False
    return True

