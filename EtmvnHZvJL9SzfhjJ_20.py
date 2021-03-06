
def strip_url_params(url, *args):
    params_to_strip = []
    for param in args:
        params_to_strip += param
    start_of_params = url.find("?")
    if start_of_params > -1:
        param_statements = get_params(start_of_params,url)
        param_dictionary = filter_params(param_statements, params_to_strip)
        url_without_params = url[0:start_of_params+1]
        for param, value in sorted(param_dictionary.items()):
            url_without_params += "" + param + "=" + value + "&"
        return url_without_params[0:-1]
    else:
        return url
​
def get_params(params_start, url):
    param_substring = url[(params_start+1)::]
    param_statements = param_substring.split("&")
    return param_statements
​
def filter_params(param_statements, params_to_strip):
    param_dictionary = {}
    for statement in param_statements:
        split_statement = statement.split("=")
        param_name = split_statement[0]
        param_value = split_statement[1]
        if param_name not in params_to_strip:
            param_dictionary[param_name] = param_value
    return param_dictionary

