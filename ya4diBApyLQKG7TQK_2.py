
import re
validate_relationships=lambda t:eval(re.sub(r'(\d=)',r'\1=',t))

