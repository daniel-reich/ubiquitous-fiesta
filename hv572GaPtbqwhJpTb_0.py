
def elasticize(word):
    return ''.join(c*(i+1 if i < len(word)/2 else len(word)-i)\
        for i, c in enumerate(word))

