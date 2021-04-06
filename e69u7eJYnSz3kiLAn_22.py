
from hashlib import sha256
def hash_ops(lst):
    sorted_hash = sorted(list(sha256(''.join(lst).encode()).hexdigest()), key=lambda c: c.isnumeric())
    return sha256(''.join(sorted_hash).encode()).hexdigest()

