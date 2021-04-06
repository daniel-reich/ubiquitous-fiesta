
def strip_url_params(url, params_to_strip=[]):
    qi = url.find('?')
    if qi < 0: return url
    params = {n:v for n,v in [p.split('=') for p in url[qi+1:].split('&') if not p[0] in params_to_strip]}
    return url[:qi+1] + '&'.join(p+'='+v for p,v in sorted(params.items()))

