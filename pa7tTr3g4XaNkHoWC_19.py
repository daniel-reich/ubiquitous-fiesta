
def pig_latin_sentence(sentence):
    vowels = "aeiou"
    pig = ""
    for word in sentence.split():
        if word[0] in vowels:
            pig += word + "way "
        else:
            word = list(word)
            while word[0] not in vowels:
                word.append(word[0])
                word.pop(0)
            pig += "".join(word) + "ay "
    return pig[ : -1]

