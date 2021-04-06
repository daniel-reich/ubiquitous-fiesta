
import hashlib
def hash_ops(lst):
​
    hashed = hashlib.sha256(''.join(lst).encode()).hexdigest()
    hashed = ''.join(sorted(hashed, key=str.isdigit))
    return hashlib.sha256(hashed.encode()).hexdigest()

