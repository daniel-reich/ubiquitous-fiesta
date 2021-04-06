
import re
​
​
def is_vowel_sandwich(s):
    return re.match(r'^[^aeiou][aeiou][^aeiou]$', s) is not None

