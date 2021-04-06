
import re
​
def small_favor(sentence):
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    lens = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
​
    def subs(m):
        mon = int(m.group(2))
        if 0 < mon < 13 and 0 < int(m.group(1)) <= lens[mon-1]:
            return m.group(0)[:-2] + ('20' if int(m.group(3)) <= 25 else '19') + \
                m.group(0)[-2:]
        return m.group(0)
​
    def subs2(m):
        mon = months.index(m.group(1))+1
        if 0 < mon < 13 and 0 < int(m.group(2)) <= lens[mon-1]:
            return m.group(0)[:-2] + ('20' if int(m.group(3)) <= 25 else '19') + \
                m.group(0)[-2:]
        return m.group(0)
    
    sentence = re.sub(r'(\d\d)[\/\.](\d\d)[\/\.](\d\d)', subs, sentence)
    sentence = re.sub('({}), (\d\d)\. (\d\d)'.format('|'.join(months)), subs2, sentence)
​
    return sentence

