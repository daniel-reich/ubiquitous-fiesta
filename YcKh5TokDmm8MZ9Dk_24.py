
def hidden_anagram(text, phrase):
    textClean = ''.join([i.lower() for i in text if i.isalpha()])
    phraseClean = ''.join([i.lower() for i in phrase if i.isalpha()])
    
    ngrams = [textClean[i:i+len(phraseClean)] for i in range(len(textClean)-(len(phraseClean)-1))]
​
    for i in ngrams:
        if sorted(i) == sorted(phraseClean):
            return i
                  
    return 'noutfond'

