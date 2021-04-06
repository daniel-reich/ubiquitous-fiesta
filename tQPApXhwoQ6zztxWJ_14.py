
import re
​
def get_prices(lst):
    l_return = []
​
    for item in lst:
        price = re.search("\d?\d\.\d\d", item)
        l_return.append(float(price.group()))
​
    return l_return

