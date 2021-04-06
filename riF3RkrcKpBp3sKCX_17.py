
import re
def cap_space(txt):
    return re.findall('[a-z]+', txt)[0] + ' ' + ' '.join(re.findall('[A-Z][a-z]+', txt)).lower()

