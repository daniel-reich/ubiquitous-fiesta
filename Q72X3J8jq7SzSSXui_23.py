
def sentence_searcher(txt, target):
    '''
    Returns the 1st sentence in txt containing target or empty string if there
    is not one.
    '''
    sentences = [''.join(s.strip()+'.') for s in txt.split('.') if target.lower() in s.lower()]
​
    return sentences[0] if sentences else ''

