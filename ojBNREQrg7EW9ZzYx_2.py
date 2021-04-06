
import re
​
def count_eatable_chocolates(money, cost):
    money, cost = map(int, re.findall('[0-9-]+', money + cost))
    if money <= 0 or cost <= 0:
        return 'Invalid Input'
    chocs = money//cost
    total = chocs
    while chocs >= 3:
        total += chocs//3
        chocs = chocs//3 + chocs%3
    return total

