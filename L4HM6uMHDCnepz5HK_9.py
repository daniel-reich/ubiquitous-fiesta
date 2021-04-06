
import re
​
def halloween(dt):
    return "Bonfire toffee" if re.search('10/31', dt) else "toffee"

