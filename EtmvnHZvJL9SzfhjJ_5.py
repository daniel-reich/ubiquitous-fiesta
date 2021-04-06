
def strip_url_params(url, params_to_strip = None):
    lst_url = url.split("?")
    if len(lst_url) == 1:
        return url
    main_url = lst_url[0] + "?"
    params = lst_url[1].split("&")
​
    if params_to_strip is not None:
        for par in params:
            key = par.split("=")[0]
            if key in params_to_strip:
                params.remove(par)
​
    params_dict = {}
    for param in params:
        key = param.split("=")[0]
        params_dict[key] = param.split("=")[1]
​
    for key,value in params_dict.items():
        full_param = key +"="+ value + "&"
        main_url += full_param
​
    return main_url[:-1]

