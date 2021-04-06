
import re
​
def split_and_delimit(txt, num, delimiter):
    pattern = '.{1,' + str(num) + '}'
    slices = re.findall(pattern, txt)
    return delimiter.join(slices)

