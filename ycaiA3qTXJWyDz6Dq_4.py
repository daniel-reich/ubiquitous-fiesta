
def consonants(word):
    consonants = 'qwrtypsdfghjklzxcvbnm'
    consonant_count = 0
​
    for letter in word:
        if letter.lower() in consonants:
            consonant_count += 1
​
    return consonant_count
  
​
def vowels(word):
    vowels = 'aeiou'
    vowel_count = 0
​
    for letter in word:
        if letter.lower() in vowels:
            vowel_count += 1
​
    return vowel_count

