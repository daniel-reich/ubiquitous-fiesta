
def parse_code(txt):
    dict_1 = {}
    result = txt.split('0')
    while '' in result:
        result.remove('')
    for i in range(len(result)):
        dict_1["first_name"] = result[0].strip('0')
        dict_1["last_name"] = result[1].strip('0')
        dict_1["id"] = result[-1].strip('0')
    return dict_1

