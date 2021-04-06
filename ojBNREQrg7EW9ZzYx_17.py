
import re
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    total = int(''.join(re.findall(r'[0-9]', total_money)))
    cost_one = int(''.join(re.findall(r'[0-9]', cost_of_one_chocolate)))
    if total == 0 or cost_one == 0:
        return 'Invalid Input'
    
    num_chocs = total/cost_one
    idx_tot = total_money.index(str(total))
    idx_one = cost_of_one_chocolate.index(str(cost_one))
​
    if total_money[idx_tot-1] == '-' or cost_of_one_chocolate[idx_one-1] == '-':
        return 'Invalid Input'
    
    ans = num_chocs + num_chocs//2
    if not num_chocs % 2:
        return ans - 1
    return ans

