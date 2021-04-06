
# https://stackoverflow.com/questions/41871841/javascript-regex-to-check-if-first-and-last-character-are-similar/41871899
# https://stackoverflow.com/questions/55097501/how-to-use-regex-to-tell-if-first-and-last-character-of-a-string-match/55097538
import re
def count_same_ends(txt):
    splitstring = txt.split()
    payload = 0    
​
    sequence = re.compile(r"^(.).*\1$", re.IGNORECASE)
    for i in splitstring:
        if i.isalpha():
            if bool(sequence.match(i)):
                payload += 1
                
        else:
             if bool(sequence.match(i[:-1])):
                  payload += 1
            
    return payload

