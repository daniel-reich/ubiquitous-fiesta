
def is_alphabetically_sorted(sentence):
    
    while(',' in sentence):
        sentence = sentence[:sentence.index(',')]+sentence[sentence.index(',')+1:]
    for word in sentence.split(' '):
        if ord(word[0])<91:
            word = chr(ord(word[0])+32) + word[1:]
        if('.' in word):
            word = word[:-1]
        if len (word) > 2:
            checker = True
            for n in range(1, len(word)):
                if ord(word[n])-ord(word[n-1])<0:
                    print(word,'false')
                    checker = False
            if checker:
                print(word,'true')
                return True
    return False

