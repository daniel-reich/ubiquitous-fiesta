
import re
def absolute(txt):
    return re.sub(r"(A|a) ", r"\1n absolute ", txt)

