
def flip(txt, spec):
    words = txt.split(" ")[::-1]
    words_reversed = txt.split(" ")
    word_result = ""
    sentence_result = ""
    for i in range(0,len(words_reversed)):
        words_reversed[i] = words_reversed[i][::-1]
    if spec == "word":
        for i in words_reversed:
            word_result += i + " "
        return(word_result[:-1])
    elif spec == "sentence":
        for i in words:
            sentence_result += i + " "
    return(sentence_result[:-1])

