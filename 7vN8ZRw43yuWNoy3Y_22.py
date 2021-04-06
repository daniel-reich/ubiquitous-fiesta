
import re
def parse_code(txt):
    match=re.match("(?P<first_name>[A-Za-z]+)0{1,}(?P<last_name>[A-Za-z]+)0{1,}(?P<id>\d+)",txt)
    return match.groupdict()

