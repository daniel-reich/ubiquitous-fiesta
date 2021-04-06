
def hidden_anagram(text, phrase):
    strippedText = ''.join([char.lower() for char in text if char.isalpha() is True])
    strippedPhrase = ''.join([char.lower() for char in phrase if char.isalpha() is True])
    phraseLetters = {letter: strippedPhrase.count(letter) for letter in strippedPhrase}
    for i in range(len(strippedText) - len(strippedPhrase) + 1):
        chunkLetters = {letter: strippedText[i: i + len(strippedPhrase)].count(letter) for letter in strippedText[i: i + len(strippedPhrase)]}
        if chunkLetters == phraseLetters:
            return strippedText[i: i + len(strippedPhrase)]
    else:
        return "noutfond"

