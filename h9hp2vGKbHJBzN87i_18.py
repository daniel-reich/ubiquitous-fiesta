
def partially_hide(phrase):
    hidden = []
    for word in phrase.split():
        first = word[0]
        middle = "-" * (len(word) - 2)
        last = word[-1]
        hidden.append(first + middle + last)
    return " ".join(hidden)

