
import re
​
def is_vowel_sandwich(s):
  return bool(re.match("^[^aeiou][aeoiu][^aeiou]$" , s , re.IGNORECASE));

