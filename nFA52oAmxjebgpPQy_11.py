
def char_index(word, char):
    try:
        last = [word.rindex(char)]
        first = [list(word).index(char)]
        index = first + last
        return index
    except ValueError:
        return None

