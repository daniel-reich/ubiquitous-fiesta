
import re
​
def kix_code(addr):
    parts = re.search(r'(\d+.*), (\d{4}) (\w{2})', addr)
    fill = re.sub(r'\W', 'X', parts.group(1))
    kix = '{}{}{}'.format(parts.group(2), parts.group(3), fill.upper())
    return kix

