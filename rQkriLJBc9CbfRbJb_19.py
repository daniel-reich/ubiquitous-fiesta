
def index_of_caps(word):
    return list(filter(lambda t:t != None,[i if word[i].isupper() else None for i in range(len(word))]))

