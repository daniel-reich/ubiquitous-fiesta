
def most_common_words(text,n):
    '''
    Returns a dictionary of the n most common words in text as per
    instructions
    '''
    tidy_up = lambda x: x.lower().replace('.','').replace(',','').replace('?','')\
              .replace('!','')
​
    words = [(tidy_up(w),i) for i,w in enumerate(text.replace("'",' ').split())]
    freqs = {}
    for word in words[::-1]:
        entry = freqs.get(word[0],(0,0))
        freqs[word[0]] = (entry[0]+1,word[1])
​
    freqs = sorted(freqs.items(),key=lambda x:(-x[1][0],x[1][1]))[:n]
    return {w[0]:w[1][0] for w in freqs}

