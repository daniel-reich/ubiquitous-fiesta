
def reverse_words(words):
    return " ".join([word for word in words.split(" ") if word != ''][::-1])

