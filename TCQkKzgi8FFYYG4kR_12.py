
import re
def camel_to_snake(s):
    return re.sub(r'[A-Z]',lambda x:"_" +x.group(0).lower(),s)

