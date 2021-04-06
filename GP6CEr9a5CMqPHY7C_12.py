
def words_to_sentence(w):
    if not bool(w) or w[0] == "":
        return ""
    if len(w) == 1:
        return w[0]
    words = [ch for ch in w if len(ch) > 0]
    if 1 < len(words) < 3:
        return "{} and {}".format(words[0], words[-1])
    return "{}, {} and {}".format(words[0], ", ".join(words[1:-1]), words[-1])

