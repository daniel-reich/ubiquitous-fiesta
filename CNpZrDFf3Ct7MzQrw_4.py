
import re
​
​
def trouble(num1, num2):
    return bool(re.search(r"(\d)\1{2,}.*,.*\1{2,}", str(num1) + "," + str(num2)))

