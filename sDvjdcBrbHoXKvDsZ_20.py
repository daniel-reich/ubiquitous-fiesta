
def anagram(name, words):
    name = name.replace(' ', '')
    name = list(name.lower())
    words = [tuple(i) for i in words]
    for word in words:
        word_letters_in_name = []
        for word_letter in word:
            if word_letter in name:
                word_letters_in_name += word_letter
                if len(word_letters_in_name) == len(word):
                    for j in word:
                        name.remove(j)
    if len(name) == 0:
        return True
    else:
        return False

