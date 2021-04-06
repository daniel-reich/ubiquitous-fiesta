
import re
def is_valid_hex_code(txt):
    match = re.findall(r'#[0-9a-fA-F]{6}',txt)
    return True if len(match) != 0 and len(txt) == 7 else False

