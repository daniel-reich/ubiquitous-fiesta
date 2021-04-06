
import re
def parse_code(txt):
    keys = ['first_name', 'last_name', 'id']
    s = re.sub('0+', ' ', txt)
    return dict(zip(keys, s.split()))

