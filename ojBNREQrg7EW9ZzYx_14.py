
import re
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
    lookfor = re.compile('\-{0,1}[0-9]{1,4}\.{0,1}[0-9]{0,2}' )
    money = float(re.findall(lookfor,total_money)[0])
    cost =  float(re.findall(lookfor,cost_of_one_chocolate)[0])
    if  cost <= 0  or   money  <= 0 or money < cost:
        return "Invalid Input"
    sets =  int((money - cost)/ (2 * cost))
    lastbars = int(((money - cost) - (2 * cost * sets))/cost)
    return  3 * sets + lastbars + 1

