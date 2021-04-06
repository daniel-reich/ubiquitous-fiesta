
def pig_latin_sentence(sentence):
    vowels = 'aeiou'
    lst = []
    for i in sentence.split():
        if i[0] in vowels:
            lst.append(i+'way')
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    lst.append(i[j:] + i[:j] +'ay')
                    break
    return ' '.join(lst)

