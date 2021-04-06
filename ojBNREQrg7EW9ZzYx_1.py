
from re import findall
def count_eatable_chocolates(total_str, cost_str):
    total = int(findall(r'-*\d+', total_str)[0])
    cost = int(findall(r'-*\d+', cost_str)[0])
    if total <= 0 or cost <= 0:
        return 'Invalid Input'
    count = total // cost
    res = count
    while count >= 3:
        res += count // 3
        count = count // 3 + count % 3
    return res

