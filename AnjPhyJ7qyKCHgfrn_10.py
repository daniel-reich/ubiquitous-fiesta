
# Fix this incorrect code, so that all tests pass!
def remove_vowels(s):
    v = "aeiouAEIOU"
    a = ""
    for i in s:
        if i not in v:
            a = a + i
    return a

