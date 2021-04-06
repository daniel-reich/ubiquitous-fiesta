
import hashlib
def hash_ops(lst):
    sha256 = hashlib.sha256((''.join(lst)).encode()).hexdigest()
    sha256 = ''.join([x for x in sha256 if x.isalpha()]+[x for x in sha256 if x.isdigit()])
    return hashlib.sha256(sha256.encode()).hexdigest()

