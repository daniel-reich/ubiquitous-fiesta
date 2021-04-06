
def duplicate_check(str_1):
    return len(list(str_1.lower())) == len(set(list(str_1.lower())))
​
​
def no_duplicate_letters(phrase):
    return all(duplicate_check(word) for word in phrase.split())

