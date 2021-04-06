
def str_to_dict(lst):
    di = dict()
    for words in lst :
        key, value = words.split('=')
        di[key] = value
    return di

