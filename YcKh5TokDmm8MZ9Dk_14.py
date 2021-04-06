
def hidden_anagram(text, phrase):
    '''
    Returns the letters in the order they appear in text if a sequence within
    text contains an anagram of phrase, or 'noutfond' if this is not the case.
    '''
    alphas = lambda x: ''.join(l for l in x.lower() if l.isalpha())
    text, phrase = alphas(text), ''.join(sorted(alphas(phrase)))
    size1, size2 = len(text), len(phrase)
​
    anagram = [text[i:i+size2] for i in range(0,size1-size2+1)
                      if ''.join(sorted(text[i:i+size2])) == phrase]
​
    #print('anagram', anagram)
    return anagram[0] if anagram else 'noutfond'

