
import re
​
def syllabification(word):
    con = 'pbtdkgG?fvszSZxhcjmnrly'
    vow = 'aAeiou'
    result = re.findall('[{}][{}][{}]?[{}]?(?=[{}]|$)'.format(con,vow,con,con,con),word)
    return '.'.join(result)

