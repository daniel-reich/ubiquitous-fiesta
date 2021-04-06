
import re
def split_and_delimit(txt, num, delimiter):
    return_value = '{}'.format(delimiter).join(i for i in re.findall('.'*num,txt))
    value = len(txt) % num
    if value != 0:
        return_value += delimiter + txt[len(txt) - value:]
    return return_value

