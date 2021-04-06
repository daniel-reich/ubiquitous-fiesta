
import re
​
​
def count_eatable_chocolates(choc, price):
    if "0" in price or "-" in price:
        return "Invalid Input"
    money, cost = int(re.findall(r"\d+", choc)
                      [0]), int(re.findall(r"\d+", price)[0])
    total = money // cost
    wrapper = money // cost
    while wrapper >= 3:
        total += wrapper // 3
        wrapper = wrapper % 3 + wrapper // 3
    return total

