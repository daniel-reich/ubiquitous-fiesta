
def word_builder(letters, positions):
    res = []
    for i in range(len(letters)):
        res.append([letters[i],positions[i]])
    res.sort(key=lambda x:x[1])
    return  ''.join(list(map(lambda x:x[0],res)))

