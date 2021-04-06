
import re
parse_code=lambda t:dict(zip(['first_name','last_name','id'],re.split('0+',t)))

