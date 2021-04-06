
import re
def kix_code(addr):
    kix = re.findall(r'((?:\d+.*(?=,))|(?:\d+ [A-Z]{2}))', addr)
    return kix[1].replace(' ', '') + re.sub(r'[^\w]+', 'X', kix[0].upper())

