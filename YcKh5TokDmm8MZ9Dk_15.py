
def hidden_anagram(text, phrase):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    phrase = "".join(sorted(phrase.lower().replace(" ","",phrase.count(" "))))
    text = list(text.lower())
    text = "".join([i for i in list(text) if i.isalpha() == True]).lower()
    counter = 0
    for i in range(0,len(text)):
        if "".join(sorted(text[counter:len(phrase)+counter])) == phrase:
            return text[counter:len(phrase)+counter]
        else:
            counter += 1 
    return "noutfond"

