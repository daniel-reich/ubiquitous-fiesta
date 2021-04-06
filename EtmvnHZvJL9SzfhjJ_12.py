
import re
from collections import OrderedDict
def strip_url_params(url: str, params_to_strip=None) -> str:
    params_in_url = re.sub(r'(.+\?)', '', url)
    if params_in_url == url:
        return url
    dict_for_it = {}
    for param in params_in_url.split('&'):
        dict_for_it[param[0]] = param[2]
    sorted_dict = OrderedDict(sorted(dict_for_it.items(), key=lambda t: t[0]))
    if params_to_strip is None:
        return 'https://edabit.com?' + '&'.join(letter + "=" + number for letter, number in sorted_dict.items())
    else:
        for key in list(sorted_dict.keys()):
            if key in params_to_strip:
                sorted_dict.pop(key)
        return 'https://edabit.com?' + '&'.join(letter + "=" + number for letter, number in sorted_dict.items())

