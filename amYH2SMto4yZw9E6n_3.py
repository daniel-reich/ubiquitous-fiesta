
from re import match
def validate(num, sep='(\)?[./() -]\(?)?'):
    return bool(match(sep.join(['(\+?\d)?', '\d{3}', '\d{3}', '\d{4}']), num))

