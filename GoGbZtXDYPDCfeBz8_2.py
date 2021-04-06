
import re
​
def magic(s):
​
    date = re.search(r'(\d+)\s(\d+)\s(\d+)', s)
    day, month, year = int(date.group(1)), int(date.group(2)), date.group(3)
    dd_mm = str(day * month)
​
    if dd_mm == year[-len(dd_mm):]:
        return True
    else:
        return False

