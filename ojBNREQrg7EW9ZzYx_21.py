
import re
​
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    pattern = re.compile(r"(-?\d+) *(\$|dollars)")
    money = int(pattern.findall(total_money)[0][0])
    cost = int(pattern.findall(cost_of_one_chocolate)[0][0])
    if money < 0 or cost <= 0:
        return "Invalid Input"
    
    total = money//cost
    wrappers = total
    while wrappers >= 3:
        wrappers -= 2
        total += 1
    return total

