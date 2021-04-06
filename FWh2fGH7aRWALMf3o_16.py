
def cleave(string,lst):
    phrase = cleaveHelper(string,lst,[])
    if phrase:
        return ' '.join(phrase)
    else:
        return "Cleaving stalled: Word not found"
​
def cleaveHelper(string,words,lst):
    if len(string) == 0:
        return lst
    if len([i for i in words if i in string]) == 0:
        return None
    else:
        letter = string[0]
        options = []
        for word in words:
            l = len(word)
            if string[:l] == word:
                options.append(word)
        if len(options) == 1:
            l = len(options[0])
            lst.append(options[0])
            string = string[l:]
            return cleaveHelper(string,words,lst)
        else:
            for option in options:
                l = len(option)
                result = cleaveHelper(string[l:],words,lst+[option])
                if result:
                    return result

