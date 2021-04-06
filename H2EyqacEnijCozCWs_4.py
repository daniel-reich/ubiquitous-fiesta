
import re
def first_n_vowels(txt, n):
    match = re.findall("[aeiou]", txt)
    return "".join(match)[:n] if (match and len(match) >= n) else "invalid"

