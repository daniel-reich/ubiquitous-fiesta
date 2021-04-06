
# Fix this incorrect code, so that all tests pass!
def remove_vowels(string):
    a = []
    vowels = "aeiou"
    for vowel in string.lower():
        if vowel not in vowels:
            a.append(vowel)
    return ''.join(a)
​
​
print(remove_vowels('hello'))

