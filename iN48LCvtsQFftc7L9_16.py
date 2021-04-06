
def word_search(letters, words):
    matrix = [list(letters[i:i+8].lower()) for i in range(0, len(letters), 8)]
    strings = []
    for i in matrix:
        strings.append(''.join(i))
    for i in range(8):
        strings.append(''.join([a[i] for a in matrix]))
        strings.append(''.join([matrix[i+a][a] for a in range(8-i)]))
        strings.append(''.join([matrix[a][a+i] for a in range(8-i)]))
        strings.append(''.join([matrix[i-a][a] for a in range(i+1)]))
        strings.append(''.join([matrix[i+a][7-a] for a in range(8-i)]))
    for i in words:
        if not any([i in a or i[::-1] in a for a in strings]):
            return False
    return True

