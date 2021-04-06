
def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url
    result,s2 = url.split('?')
    result += '?'
    s2 = [i.split('=') for i in s2.split('&')]
    d = {i[0]:i[1] for i in s2}
    for i in sorted(d.keys()):
        if i not in params_to_strip:
            result += '{}={}&'.format(i,d[i])
    return result[:-1]

