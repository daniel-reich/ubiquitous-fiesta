
import re
def parse_code(lst):
    return {x:y for x,y in zip(["first_name", "last_name", "id"], re.findall(r'[^0]+', lst))}

