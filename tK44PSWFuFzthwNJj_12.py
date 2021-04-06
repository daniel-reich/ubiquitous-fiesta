
import string
​
def club_entry(word):
    w = ""
    for i in range(len(word)):
        if word[i-1] == word[i]:
            w = word[i]
    return (string.ascii_lowercase.index(w)+1)*4

