
import re
​
def clean_up(files, sort):
    all_names = ':'.join(files)
    ans, s = [], []
    if sort == 'prefix':
        for i in re.findall(r'\w+(?=\.)', all_names):
            if i not in s:
                s.append(i)
        for i in s:
            ans.append(re.findall('{0}[^\:]+'.format(i), all_names))
    else:
        for i in re.findall(r'(?<=\.)\w+', all_names):
            if i not in s:
                s.append(i)
        for i in s:
            ans.append(re.findall('\w+\.{0}'.format(i), all_names))
    return ans

