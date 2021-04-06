
from re import sub
to_camel_case = lambda s: sub(r'_(\w)', lambda x: x.group(1).upper(), s)
to_snake_case = lambda s: sub(r'\B[A-Z]', lambda x: '_' + x.group(0).lower(), s)

