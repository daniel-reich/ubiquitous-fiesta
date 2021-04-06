
def syllabification(word):
    # Approach: find the vowels, claim all the consonants before them as onsets, tack everything else into codas
    characters = list(word)
    nuclei = [
        index
        for index, character in enumerate(characters)
        if character in 'aAeiou'
    ]
    syllables = [
        characters[x]
        for x in nuclei
    ]
    for nucleus in nuclei:
        characters[nucleus] = None
    # Find onsets
    for syllable_index, nucleus in enumerate(nuclei):
        if (
            nucleus > 0 and
            characters[nucleus - 1] is not None
        ):
            syllables[syllable_index] = characters[nucleus - 1] + syllables[syllable_index]
            characters[nucleus - 1] = None
    # Find codas
    for syllable_index, nucleus in enumerate(nuclei):
        for coda_index in range(nucleus + 1, len(characters)):
            coda_character = characters[coda_index]
            if coda_character is None:
                break
            syllables[syllable_index] += coda_character
    return '.'.join(syllables)

