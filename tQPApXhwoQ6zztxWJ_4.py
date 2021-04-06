
import re 
​
def get_prices(lst):
    priceRegex = re.compile(r"\d*\.[1-9]{0,2}")
    lst = priceRegex.findall(str(lst))
    return list(map(float, lst))

