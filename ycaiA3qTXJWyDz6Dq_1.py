
def consonants(word):
    return sum(1 for i in word if i.lower() not in 'aeiou' and i.isalpha())
​
​
def vowels(word):
    return sum(1 for i in word if i.lower() in 'aeiou')

