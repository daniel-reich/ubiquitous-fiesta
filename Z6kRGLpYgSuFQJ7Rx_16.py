
def find_longest(sentence):
    sentence = sentence.replace("'", " ").replace("."," ")
    return sorted(sentence.split(" "), key=lambda x: len(x))[-1].lower()

