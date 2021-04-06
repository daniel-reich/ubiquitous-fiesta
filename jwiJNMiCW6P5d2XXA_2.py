
import re
​
def does_rhyme(txt1, txt2):
    
    vowels = r'[aeiouAEIOU]'
    txt1_last_word_vowels = ''.join(re.findall(vowels, txt1.split()[-1]))
    txt2_last_word_vowels = ''.join(re.findall(vowels, txt2.split()[-1]))
​
    return txt1_last_word_vowels.lower() == txt2_last_word_vowels.lower()

