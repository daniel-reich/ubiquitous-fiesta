
import re
repeated=lambda s:bool(re.match(r"(\w+)\1+$",s))

