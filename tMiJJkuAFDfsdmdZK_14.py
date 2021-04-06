
import re
​
​
def to_snake_case(txt):
    return '_'.join(re.findall('[A-Z]?[a-z]+', txt)).lower()
​
​
def to_camel_case(txt):
    b = re.findall(r'[a-z]+', txt)
    return b[0] + ''.join([element.title() for element in b[1:]])

