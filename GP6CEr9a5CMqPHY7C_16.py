
def words_to_sentence(words):
    if words:
        words = [s for s in words if s != ""]
    if not words:
        return ""
    words = [s for s in words if s != ""]
    if len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return "{} and {}".format(*words)
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

