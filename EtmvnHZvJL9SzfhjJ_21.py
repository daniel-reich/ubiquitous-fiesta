
import re
​
def strip_url_params(url, to_strip=None):
    if not to_strip:
        to_strip = []
    res = []
    if '?' not in url:
        return url
    for param in reversed(re.findall(r'[?&]([^&]+)', url)):
        k, v = param.split('=')
        if k not in to_strip:
            to_strip.append(k)
            res.append(param)
    if res:
        return url[:url.index('?')+1] + '&'.join(sorted(res))
    else:
        return url[:url.index('?')]

