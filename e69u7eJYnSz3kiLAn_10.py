
import hashlib
def enc(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
​
def hash_ops(lst):
    a = enc(''.join(lst))
    sortt = ''.join([x for x in a if x.isalpha()] + [x for x in a if x.isdigit()])
    return enc(sortt)

