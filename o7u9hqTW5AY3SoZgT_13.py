
def switch(word):
    '''
    Replaces the end of a word - ignoring punctuation - by 'nts' if it is 'nce'
    and vice versa then returns it.
    '''
    alpha_word = ''.join([l for l in word if l.isalpha()])
    if alpha_word.endswith('nce'):
        alpha_word = alpha_word[:-3] + 'nts'
    elif alpha_word.endswith('nts'):
        alpha_word = alpha_word[:-3] + 'nce'
​
    return alpha_word + word[len(alpha_word):]  # restore any punctuation
        
                         
def switcheroo(sentence):
    '''
    Returns sentence with 'nts' replaced by 'nce' and vice versa if they are at
    the end of a word as per the instructions.
    '''
    return ' '.join(switch(word) for word in sentence.split())

