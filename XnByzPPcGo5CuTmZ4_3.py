
import re
​
def kix_code(addr):
    s = re.match('.*?, .*? (?P<third>\d+?.+?), (?P<first>\d+?) (?P<second>\w+?) .*',addr)
    third = s.group('third').upper()
    for i in third:
        if not i.isalnum():
            third = third.replace(i,'X')
    return s.group('first')+s.group('second')+third

