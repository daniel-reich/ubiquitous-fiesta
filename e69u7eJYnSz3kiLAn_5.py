
import hashlib
def hash_ops(lst):
    initial_hash = hashlib.sha256(bytes(''.join(lst), 'utf-8')).hexdigest()
    sorted_hash = ''.join(sorted(initial_hash, key=str.isdigit))
    return hashlib.sha256(bytes(sorted_hash, 'utf-8')).hexdigest()

