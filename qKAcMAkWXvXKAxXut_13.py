
import re
​
​
def calc_bundled_temp(n, temp):
    initial_temp = float(re.search('\d+', temp).group())
    for num in range(1, n+1):
        initial_temp = (initial_temp * 0.1) + initial_temp
    return str(round(initial_temp,1)) + "*C"

