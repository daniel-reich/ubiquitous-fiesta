
def constraint(text):
    '''
    Returns the type of sentence based on the above rules: Pangram, Heterogram,
    Tautogram, Transgram or Sentence.
    '''
    from string import ascii_lowercase as alphabet
    text = text.lower()
​
    if all(text.count(l) >= 1 for l in alphabet):
        return 'Pangram'
​
    if all(text.count(l) == 1 for l in text if l.isalpha()):
        return 'Heterogram'
​
    text_list = text.split()
    if all(text_list[i][0] == text_list[0][0] for i in range(1, len(text_list))):
        return 'Tautogram'
​
    for l in text_list[0]:
        common = True
        for i in range(1, len(text_list)):
            if l not in text_list[i]:
                common = False
                break
        if common:
            return 'Transgram'
​
    return 'Sentence'

