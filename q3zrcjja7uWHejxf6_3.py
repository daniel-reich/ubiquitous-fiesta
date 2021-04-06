
import re
def negative_sum(chars):
    chars =chars.replace('-',' -')
    ans= list(filter(lambda x:x!='',re.sub(r'[^-\d]',' ',chars).split(' ')))
    return sum(list(map(lambda x:int(x),(list(filter(lambda x:eval(x)<0,ans))))))

