
def markdown(symbol):
    '''
    Returns a function which allows symbol to be applied to all instances of a
    given word in a given text. If the target word has punctuation suffixing it,
    this will be included between the markdown symbols.
    '''
    
    def formatter(text, target):
        '''
        Applies symbol to all instances of target in text as per instructions.
        '''
        return ' '.join([symbol + word + symbol if word.lower().startswith(target.lower()) \
                        else word for word in text.split()])
​
    return formatter

