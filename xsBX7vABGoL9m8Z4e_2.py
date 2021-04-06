
import re
def sync_subs(subtitles, timeIncrement):
    pattern = r'[0-9]{2,2}:[0-5][0-9]:[0-5][0-9],[0-9]{3,3}'
    if not re.search(pattern, timeIncrement):
      return 'There is a problem with the second argument'
    
    lst = re.findall(pattern,subtitles)
    t = [int(i) for i in (timeIncrement.split(',')[0].split(':')+timeIncrement.split(',')[1:])[::-1]]
    for i in lst:
        a = [int(j) for j in (i.split(',')[0].split(':')+i.split(',')[1:])[::-1]]
        b = [str(k) for k in [(t[0]+a[0])%1000, ((t[0]+a[0])//1000 + t[1] + a[1])%60, (((t[0]+a[0])//1000 + t[1] + a[1])//60 + t[2] + a[2])%60, (((t[0]+a[0])//1000 + t[1] + a[1])//60 + t[2] + a[2])//60 + t[3] +a[3]][::-1]]
        c = ['0'*(2-len(i))+i for i in b[:-1]] + ['0'*(3-len(b[-1]))+b[-1]]
        d = ':'.join(c[:-1])+','+c[-1]
        subtitles = subtitles.replace(i, d)
    return subtitles

