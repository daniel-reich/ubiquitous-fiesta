
def validate_swaps(lst, txt):
    def validate_swaps_(word):
        nonmatches = [(a,b) for a,b in zip(word, txt) if a!=b]
        return  len(word) == len(txt) and len(nonmatches) == 2
    return [validate_swaps_(word) for word in lst]

