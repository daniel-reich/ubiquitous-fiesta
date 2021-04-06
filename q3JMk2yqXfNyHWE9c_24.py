
def double_letters(word):
        dub = False
        for i in range(0, len(word)-1):
                if word[i] == word[i+1]:
                        dub = True
                        break
        return dub

