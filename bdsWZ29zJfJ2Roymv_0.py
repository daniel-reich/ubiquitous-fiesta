
import re
​
def swap_two(txt):
    return re.sub(r'(.{2})(.{2})', r'\2\1', txt)

