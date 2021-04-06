
def vigenere(text, keyword):
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if " " not in text:
        text = [i.upper() for i in text if i.isalpha() == True]
        key = keyword*int((len(text)/len(keyword))+1)
        key = key.upper()
        for i in range(0,len(text)):
            letter = abc.index(text[i])-abc.index(key[i])+26
            while letter >= len(abc):
                letter -= len(abc)
            text[i] = abc[letter]
        return "".join(text)
    else:
        text = [i.upper() for i in text if i.isalpha() == True]
        key = keyword*int((len(text)/len(keyword))+1)
        key = key.upper()
        for i in range(0,len(text)):
            letter = abc.index(text[i])+abc.index(key[i])
            while letter >= len(abc):
                letter -= len(abc)
            text[i] = abc[letter]
        return "".join(text)

