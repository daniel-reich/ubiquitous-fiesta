
def is_alpha(word):
    return True if sum(ord(letter.lower()) + 1 - ord("a") for letter in word if letter.isalpha()) % 2 == 0 else False

