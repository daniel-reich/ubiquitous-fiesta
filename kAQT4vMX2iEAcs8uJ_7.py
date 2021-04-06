
import re
def longest_7segment_word(lst):
    valid_word=[]
    for word in lst:
       if re.search('[kmvwx]',word)==None:
          valid_word.append(word)
       else:
          continue
    return max(valid_word,key=len,default="")

