
import re
pattern = re.compile(r'[1-9]\d*\.\d*|[1-9]\d*[1-9]|[1-9]')
def sig_figs(num):
    return (len(re.sub(r'\.', '', pattern.findall(num)[0]))
            if bool(pattern.search(num)) else 0)

