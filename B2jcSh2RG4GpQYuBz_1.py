
import re
is_valid_phone_number=lambda t:bool(re.match("^\(\d{3}\) \d{3}-\d{4}$",t))

