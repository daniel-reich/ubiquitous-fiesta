
import re
​
​
​
def common_last_vowel(txt):
    vowels = "aeiouAEIOU"
    counts = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for word in txt.split():
        word = ''.join([letter for letter in word if letter.isalpha()])
        if word[-1] in vowels:
            counts[word[-1].lower()] += 1
        else:
            matches = re.findall(r"[aeiouAEIOU]", word)
            if len(matches) == 1:
                counts[matches[0].lower()] += 1
    return max([(letter, total) for letter, total in counts.items()], key=lambda x: x[1])[0]

