
import re
def dakiti(sentence):
    sentence= sorted(sentence.split(' '),key=lambda x:int(re.findall(r'\d',x)[0]))
    return ' '.join(list(map(lambda x:re.sub(r'\d','',x),sentence)))

