
from collections import OrderedDict
def strip_url_params(url, params_to_strip=[]):
  # Get search parameters
    try:
        params = url[url.index('?'):]
    except ValueError:
        return url
    params = params[1:].split('&')
    p_dic = OrderedDict()
    for p in params:
        p = p.split('=')
        p_dic[p[0]] = p[1]
    for para in params_to_strip:
        if para in p_dic.keys():
            del(p_dic[para])
    param_string = '?' + '&'.join([key + '=' + value for key, value in p_dic.items()])
    return url[:url.index('?')] + param_string

