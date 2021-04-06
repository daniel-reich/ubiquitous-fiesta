
def rotated_words(txt):
    rotate_letters = ["H", "I", "N", "M", "O", "S", "W", "X", "Z"]
    words = set(txt.split())
    full_rot_words = 0
    for w in words:
        rotated_letters = 0
        for x in w:
            if x.upper() in rotate_letters:
                rotated_letters += 1
        if len(w) == rotated_letters:
            full_rot_words += 1
    return full_rot_words

