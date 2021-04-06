
import re
months = {'January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December'}
def small_favor(sentence):
    def rep(m):
        s = m.group()
        if len(s) == 8:
            return s[:6] + ('20' if int(s[6:]) < 25 else '19') + s[6:]
        if s[:s.index(',')] in months:
            return s[:-3] + ('20' if int(s[-3:-1]) < 25 else '19') + s[-3:]
        return s
​
    res = re.sub(r'(\b\w{3,9}, \d\d. \d\d.)|((\d\d[/.]){2}\d\d)', rep, sentence)
    return res

