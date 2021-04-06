
import re
​
​
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    total_money = int(re.findall(r'-?\d+', total_money)[0])
    cost_of_one_chocolate = int(re.findall(r'-?\d+', cost_of_one_chocolate)[0])
    if cost_of_one_chocolate <= 0 or total_money < 0:
        return 'Invalid Input'
    current_eatable_chocolates = total_money // cost_of_one_chocolate
    total_eatable_chocolates = 0
​
    while current_eatable_chocolates > 0:
​
        if current_eatable_chocolates >= 3:
            current_eatable_chocolates -= 3
            total_eatable_chocolates += 3
            current_eatable_chocolates += 1
​
        else:
            total_eatable_chocolates += current_eatable_chocolates
            break
​
    return total_eatable_chocolates

