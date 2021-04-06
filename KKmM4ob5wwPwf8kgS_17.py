
def get_frequencies(lst):
    unique = set(lst)
    dictionary = {}
    for i in unique:
        dictionary[i] = len([double for double in lst if double == i])
    return dictionary

