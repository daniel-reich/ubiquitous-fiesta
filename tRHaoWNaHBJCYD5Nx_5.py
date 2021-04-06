
def same_letter_pattern(txt1, txt2):
​
    if len(txt1) != len(txt2):
        return False
    
    codes = {}
​
    for char1, char2 in zip(txt1, txt2):
        if char1 not in codes:
            codes[char1] = char2
        else:
            if codes[char1] != char2:
                return False
​
    return True

