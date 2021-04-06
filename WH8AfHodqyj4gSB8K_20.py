
import re
def is_authentic_skewer(s):
    vowels = 'aeiouAEIOU'
​
    # First and Last character MUST NOT be vowel
    if s[0] in vowels or s[-1] in vowels:
        return False
​
    # If no alpha OR no symbols, we need to return False
    if not re.search('[a-zA-Z]', s) or not re.search('[^a-zA-Z]', s):
        return False
​
    # Find the separator
    start_idx = re.search("[^a-zA-Z]", s).start()
    idx = start_idx + 1
    while s[idx] == s[start_idx]:
        idx += 1
    end_idx = idx
    sep = s[start_idx:end_idx]
​
    # Get the split string
    split_str = s.split(sep)
​
    # Split string should contains only alphabets
    # and MUST NOT contain any empty strings
    if not all(map(str.isalpha, split_str)):
        return False
​
    # Check for consonant in even positions and vowels in odd
    for index, char in enumerate(split_str):
        if index%2 == 0 and char in vowels:
            return False
        elif index%2 and char not in vowels:
            return False
    return True

