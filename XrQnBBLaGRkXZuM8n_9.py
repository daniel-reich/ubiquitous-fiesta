
def index_filter(indexes, string):
    wordAsList = [string[x].lower() for x in indexes]
    return ''.join(wordAsList)

