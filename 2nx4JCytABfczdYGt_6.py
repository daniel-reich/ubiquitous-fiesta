
pronouns = {1: "Io", 2: "Tu", 3: "Egli", 4: "Noi", 5: "Voi", 6: "Essi"}
suffixes = {1: "o", 2: "i", 3: "a", 4: "iamo", 5: "ate", 6: "ano"}
​
def conjugate(verb, pronoun):
    assert verb[-3:] == "are"
    root = verb[:-3]
    if pronoun in [1, 3, 5, 6]:
        ans = pronouns[pronoun] + ' ' + root + suffixes[pronoun]
    else:
        if root[-1] in ['c', 'g']:
            ans = pronouns[pronoun] + ' ' + root + 'h' + suffixes[pronoun]
        elif root[-1] == 'i':
            ans = pronouns[pronoun] + ' ' + root + suffixes[pronoun][1:]
        else:
            ans = pronouns[pronoun] + ' ' + root + suffixes[pronoun]
    return ans

