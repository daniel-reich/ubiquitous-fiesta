
def alternating_caps(string):
    word, index, spaces_position, space_index = list(string.lower()), 0, [], 0
    for i in word:
        if i == " ":
            spaces_position.append(space_index)
        space_index += 1
    for i in range(0,string.count(" "),1):
        word.remove(" ")
    for i in word:
        if index == 0 or index % 2 == 0:
            word[index] = i.upper()
        index+=1
    for i in spaces_position:
        word.insert(i, " ")
    return "".join(word)

