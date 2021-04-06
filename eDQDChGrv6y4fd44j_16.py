
def can_put(txt, dim):
    words = [len(word) for word in txt.split()]
    for _ in range(dim[0]):
        line_size = dim[1]
        for i, word_size in enumerate(words):
            if dim[1] < word_size:
                return False
            if line_size < word_size:
                break
            else:
                line_size -= word_size + 1
                words = words[i+1:]
    return not words

