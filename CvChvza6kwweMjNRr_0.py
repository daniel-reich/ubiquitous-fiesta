
import re
​
def split_code(item):
    parts = re.search(r'(\D*)(\d*)', item)
    return [parts.group(1), int(parts.group(2))]

