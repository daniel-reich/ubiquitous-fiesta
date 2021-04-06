
import re
​
letter_regex = re.compile(r'\b(\w)\.')
word_regex = re.compile(r'(\w+)[!.?]$')
​
​
def validate_spelling(txt):
    letters = (''.join(letter_regex.findall(txt)))
    words = (''.join(word_regex.findall(txt)))
    if letters.lower() == words.lower():
        return True
    return False

