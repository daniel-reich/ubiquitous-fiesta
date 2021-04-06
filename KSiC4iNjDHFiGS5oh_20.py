
import re
def is_super_d(num):
    result = "Normal Number"
    nums = [d*num**d for d in range(10)]
    for i, n in enumerate(nums):
        if re.findall(str(i)*i, str(n)) and i > 1:
            result = "Super-" + str(i) + " Number"
            break
    return result

