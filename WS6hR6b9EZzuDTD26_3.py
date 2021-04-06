
def no_duplicate_letters(phrase):
    phrase_lst = phrase.split()
    return all([True if len(set(word.lower())) == len(word.lower()) else False for word in phrase_lst])

