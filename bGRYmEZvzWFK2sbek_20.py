
import string
def get_missing_letters(s):
    abc = string.ascii_lowercase
    return ''.join(sorted([x for x in abc if x not in s]))

