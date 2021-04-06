
import re
​
def strip_url_params(url, params_to_strip = []):
    # Disassemble url
    url_parts = re.split('\?', url)
    params_dict = {}
    new_url_parts = [url_parts[0]]
​
    # Extract all unique params
    if len(url_parts) > 1:
        params = re.split('&', url_parts[1])
        for s in params:
            param_parts = re.split('=', s)
            params_dict[param_parts[0]] = param_parts[1]
​
    # Remove params_to_strip from the map
    for param in params_to_strip:
        params_dict.pop(param, None) 
​
    if len(params_dict.keys()) > 0: new_url_parts.append('?')
​
    # Re-assemble url
    for key in sorted(params_dict.keys()):
        new_url_parts.append(key + '=' + params_dict[key])
        
    # Put a &-character in-between the params
    for i in range(2, len(new_url_parts) - 1):
        new_url_parts[i] += '&'
​
    return ''.join(new_url_parts)

