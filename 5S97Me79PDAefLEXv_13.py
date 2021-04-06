
import re
def lambda_to_def(code):
    m = re.match(r"^(\w+)\s*=\s*lambda\s+(.*?(?:'.*')?(?=:)):\s*(.*)$", code)
    return 'def {}({}):\n\treturn {}'.format(m.group(1), m.group(2), m.group(3))

