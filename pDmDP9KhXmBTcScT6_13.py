
import re
def get_name(address):
    address = address.split('@')[0]
    return ''.join((re.findall(r'[a-z]',address,flags=re.I)))

