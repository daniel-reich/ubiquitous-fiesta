
import re
​
def remove_vowels(txt):
    return re.sub(r'[aeiou]+', '', txt, flags=re.IGNORECASE)

