
def extend_vowels(word, num):
    if num < 0 or type(num) is not int:
        return "invalid"
    return "".join(c * (num + 1) if c in "aeiouAEIOU" else c for c in word)

