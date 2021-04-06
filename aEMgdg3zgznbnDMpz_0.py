
import re
def rotated_words(txt):
     return len(set(re.findall(r"\b[HINOSXZMW]+\b", txt)))

