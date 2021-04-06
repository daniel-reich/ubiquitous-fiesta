
def no_strangers(text):
    '''
    Analyses text and returns 2 lists: acquaintances for words which occur 3 to
    4 times, friends for those which occur 5+ times. Words are ordered by the
    order in which words first become acquaintances or friends.
    '''
    import re
​
    def rank(words, min_val, max_val, idx):
        '''
        Returns a list containing the words in words whose frequency lie
        between min_val and max_val, sorted by the position at idx.
        '''
        selected = {word: [] for word in words if min_val <= words.count(word) <= max_val}
        for i, word in enumerate(words):
            if word in selected:
                selected[word].append(i)  # store locations of selected words
​
        return sorted((word for word in selected), key=lambda x: selected[x][idx]) 
​
    words = [word.lower() for word in re.split("[^A-Za-z0-9']+", text)]
    words = [word for word in words if word != '']  # remove empty strings
    
    return [rank(words, 3, 4, 2), rank(words, 5, len(words)+1, 4)]

