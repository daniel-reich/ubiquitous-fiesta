
import re
def constraint(text):
    text=text.lower()
    text1=text.split(' ')
    text2=[set(x) for x in text1]
    if len(set(re.findall(r'[a-zA-Z]', text)))==26:
        return 'Pangram'
    elif len(re.findall(r'[a-zA-Z]', text))==len(set(re.findall(r'[a-zA-Z]', text))):
        return 'Heterogram'
    elif len(set(x[0] for x in text1))==1:
        return 'Tautogram'
    elif len(text2[0].intersection(*text2)) > 0:
        return 'Transgram'
    else:
        return "Sentence"

