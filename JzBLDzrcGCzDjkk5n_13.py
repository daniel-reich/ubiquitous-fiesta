
def encrypt(word):
    if word == "":
        return None
    rev_wrd = word[::-1]
    vowels = {"a": 0, "e": 1, "o": 2, "u": 3}
    mapping_func =lambda x: str(vowels[x]) if x in vowels  else x
    return ''.join(map(mapping_func, rev_wrd)) + "aca"

