
def can_put(message, dimensions):
    def fit_word(pointer, word):
        height, width = dimensions
        row, col = pointer
        if width - col >= len(word): #fits in line
            return (row, col + len(word) + 1)
        elif row + 1 < height and len(word) <= width:
            return (row + 1, len(word) + 1)
​
    pointer = (0,0)
    for word in message.split():
        pointer = fit_word(pointer, word)
        if not pointer:
            return False
    return True

