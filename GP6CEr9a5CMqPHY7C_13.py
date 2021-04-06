
def words_to_sentence(words):
    if  words==None:return ''
    words = list(filter(lambda x:x!='',words))
    if len(words)==0:return ''
    elif len(words)==1:return words[0]
    elif len(words)==2:return ' and '.join(words)
    else:
        return ', '.join(words[:len(words)-1]) + ' and '+ words[-1]

