
import re
is_zygodrome = lambda x: not re.sub(r'(\d)\1+', '', str(x))

