
import hashlib
​
def hash_ops(lst):
    h = hashlib.sha256(''.join(lst).encode('utf-8')).hexdigest()
    letters = [c for c in h if 'a' <= c <= 'z']
    digits = [c for c in h if '0' <= c <= '9']
    s = ''.join(letters + digits)
    h2 = hashlib.sha256(s.encode('utf-8')).hexdigest()
    return h2

