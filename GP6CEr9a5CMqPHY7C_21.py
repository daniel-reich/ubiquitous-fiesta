
def words_to_sentence(words):
    if words == None or words == [] or words == [[]]:
        return ""
    for i in range(len(words)):
        try:
            if words[i] == "":
                words.pop(i)
        except IndexError:
            pass
    output = ""
    for i in range(len(words)):
        if i == len(words)-1:
            output += words[i]
        elif i == len(words)-2:
            output += words[i] + " and "
        else:
            output += words[i] + ", "
    return output

