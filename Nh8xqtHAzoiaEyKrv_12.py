
import re
def correct_sentences(s):
    s= re.sub(r' [A-Z]',lambda x:'. '+(x.group(0)).strip(),s).strip().replace('  '," ").split('.')
    return '. '.join(list(map(lambda ss:ss.strip().capitalize().replace('  '," "),s))) + '.'

