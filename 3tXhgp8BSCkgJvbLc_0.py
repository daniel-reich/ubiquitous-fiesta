
def find_words(fragments):
    '''
    Returns a sorted list of the 20 words in DICTIONARY made from the fragments
    in fragments
    '''
    from itertools import permutations, combinations
​
    fragset = sorted(fragments)
    size = 2 if len(fragments) == 40 else 3
​
    word_set = {}
    for combo in permutations(fragset, size):
        word = ''.join(combo)
        if word in DICTIONARY:
            word_set[word] = combo
​
    if len(word_set) == 20:
        return sorted(word_set)
​
    for combo in combinations(word_set, 20):
        frag_list = sorted([frag for word in combo for frag in word_set[word]])
        if frag_list == fragset:
            return sorted(combo)
​
    return 'Error - failed to find 20 words to fit!!'

