
def cleave(string, lst):
    def words(word, string, i):
        while True:
            if string[0:i] in lst:
                word.append(string[0:i])
                string = string[i::]
                i = 0 
                if string == '':
                    break
            elif i == len(string):
                a = word.pop()
                words(word, a + string, len(a) + 1)
            elif i > len(string):
                break
            i += 1
    word = []
    try:
        words(word, string, 1)
    except:
        word = ['Cleaving stalled: Word not found']
    return ' '.join(word)

