
def is_alphabetically_sorted(sentence):
    x=['t' if i.lower()==''.join(sorted(i.lower())) else 'f' for i in sentence[:-1].split() if len(i)>=3]
    return True if 't' in x else False

