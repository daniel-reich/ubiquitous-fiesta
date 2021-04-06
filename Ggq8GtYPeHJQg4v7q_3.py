
import re
​
def replace_vowels(txt, ch):
    return re.sub(r'[aeiou]', ch, txt)

