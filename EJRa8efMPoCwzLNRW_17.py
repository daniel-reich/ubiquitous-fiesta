
import re
import string
​
def dakiti(sentence):
    dic = dict()
    finaldic = dict()
    words = sentence.split()
    i = 0
    frase = str()
    for word in words:
        number = re.findall('[0-9]', word)
        dic[word] = number[0]
        parts = word.split(number[0])
        palabra = parts[0]+parts[1]
        if palabra in finaldic.keys():
          palabra += '{}'.format(i)
        finaldic[palabra] = number[0]
        i+=1
    for item in sorted(finaldic.items(), key=lambda x: x[1]):
        frase += str(item[0]).rstrip(string.digits)
        frase += ' '
    return(frase.strip())

