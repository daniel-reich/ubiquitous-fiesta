
def is_smooth(sentence):
    sentence = sentence.lower().split()
    first = [first_letter[0] for first_letter in sentence]
    last = [last_letter[-1] for last_letter in sentence]
    return first[1:] == last [:-1]

