
import re
​
INITIAL = 0
WORD = 1
​
def valid_name(name):
    initial = re.compile(r'([A-Z]\.)')
    word = re.compile(r'([A-Z][a-z]+)')
    name = name.split()
​
    # Check that name is the correct length
    if len(name) not in (2, 3):
        return False
​
  # replace each part of the name with INITIAL or WORD identifiers
    for i in range(len(name)):
        if re.fullmatch(initial, name[i]):
            name[i] = INITIAL
        elif re.fullmatch(word, name[i]):
            name[i] = WORD
        else:
            # This is not a valid word or initial
            return False
​
    if len(name) == 3:
        if name[2] == INITIAL:
            # Last name can't be capitalized
            return False
        if name[0] == INITIAL and name[1] == WORD:
            # First name as initial and middle name as word is illegal
            return False
​
    return True

