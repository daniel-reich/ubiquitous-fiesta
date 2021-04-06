
def remove_punctuation(txt: str) -> str:
    """Removes punctuation marks and other non alpha characters from a string"""
    return "".join([i for i in txt if i.isalpha()])
​
​
def check_if_sorted(txt):
    return txt == ''.join(sorted(txt))
​
​
​
def is_alphabetically_sorted(sentence):
    return any([check_if_sorted(remove_punctuation(i)) for i in sentence.split() if len(i) >=
                3])

