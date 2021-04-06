
import re
def security(txt):
    ans = re.findall(r'[G|T]*x*\$x*[G|T]*',txt)
    if 'T' in ''.join(ans):
        return 'ALARM!'
    return 'Safe'

