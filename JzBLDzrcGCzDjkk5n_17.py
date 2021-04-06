
def encrypt(word):
    lookup = {'a':'0','e':'1','o':'2','u':'3'}
    final_word = ''
    for i in range(0,len(word)):
        final_word = final_word + word[len(word)-i-1]
    for i in final_word:
        if i in lookup.keys():
            final_word = final_word.replace(i,lookup[i])
    return final_word + 'aca'

