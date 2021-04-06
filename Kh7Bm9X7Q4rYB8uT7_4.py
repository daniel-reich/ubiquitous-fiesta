
def is_vowel_sandwich(word):
    vowels = ['a','e','i','o','u']
    if len(word) == 3:  
        if word[0] not in vowels and word[1] in vowels and word[2] not in vowels:
            return True
        else:
            return False
    else:
           return False

