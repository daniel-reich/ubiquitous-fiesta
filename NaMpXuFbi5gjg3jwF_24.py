
import re
def sock_pairs(socks):
  return len(re.findall(r'([A-Z])\1', ''.join(sorted(socks))))

