
def sentence(words):
    ans = "An " if words[0][0] in "aeiou" else "A "
    ans += words.pop(0)
    for word in words[:-1]:
        if word[0] in "aeiou":
            ans += ", an " + word
        else:
            ans += ", a " + word
    ans += " and "
    if words[-1][0] in "aeiou":
        ans += "an " + words[-1]
    else:
        ans += "a " + words[-1]
    return ans + "."

