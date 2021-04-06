
import re
insert_whitespace=lambda t:re.sub(r'([a-z])([A-Z])',r'\1 \2',t)

