
VOWELS = 'aeiou'
PUNCTUATION = '!.,?:;"'
​
def translate_word(word):
    '''
    Returns word translated to pig latin as per the instructions
    '''
    if not word:
        return ''
​
    size = len(word)
    if word[0] in PUNCTUATION:
        i = 1
        start_punc = 1
    else:
        i = 0
        start_punc = 0  # adjust for leading punctuation
        
    end_punc = size
    for j in range(1, size):
        if word[j] in PUNCTUATION:
            end_punc = j   # where trailing punctuation starts
            break
    
    pig = 'yay' if word[i].lower() in VOWELS else 'ay'
    capital = True if word[i].isupper() else False
    while not word[i].lower() in VOWELS:
        i += 1
        
    if capital:
        word = word[:i].lower() + word[i].upper() + word[i+1:].lower()
​
    return word[0:start_punc] + word[i:end_punc] + word[start_punc:i] + pig + word[end_punc:]
    
def translate_sentence(sentence):
    '''
    Translates sentence into pig latin as per the instructions
    '''
    return ' '.join([translate_word(word) for word in sentence.split()])

