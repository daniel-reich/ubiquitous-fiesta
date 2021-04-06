
def special_reverse(s, c):
    return " ".join([word if word[0] not in c else word[-1::-1] for word in s.split()])

