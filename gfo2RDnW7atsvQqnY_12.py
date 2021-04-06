
import re
def count_smileys(lst):
    count=0
    for i in lst:
        if re.fullmatch(r'[:|;][-|~]{0,1}[)|D]',i)!=None:
            count+=1
    return count

