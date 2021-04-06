
import re
def get_type(value):
    return re.compile(r"\'(\w+)\'").search(str(type(value))).group(1)

