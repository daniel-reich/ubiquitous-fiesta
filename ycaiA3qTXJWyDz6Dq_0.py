
def consonants(word):
    return sum(c.lower() not in 'aeiou' for c in word if c.isalpha())
​
def vowels(word):
    return sum(c.lower() in 'aeiou' for c in word)

