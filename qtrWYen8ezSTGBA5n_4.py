
def correct_spacing(sentence):
    words = sentence.split()
    new_sentence = ''
    for word in words:
        if word is words[-1]:
            new_sentence += word
        else:
            new_sentence += word + ' '
    return new_sentence

