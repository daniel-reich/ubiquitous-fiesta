
import re
def haiku(text):
    result = []   
    for verse in re.sub(r'[,.!;:\']','', text.lower()).split('/'):        
        versecnt = 0        
        for word in verse.split():
            sylcnt = 0
            for x in re.findall(r'[aeiouy]+', word):
                sylcnt = sylcnt + 1
            if sylcnt > 1 and (word[-1] == "e" or word[-2::] == "es"):
                sylcnt = sylcnt - 1              
            versecnt = versecnt + sylcnt         
        result.append(versecnt)
    return result == [5,7,5]

