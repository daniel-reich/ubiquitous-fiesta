
from hashlib import sha256
​
def hash_ops(lst):
    hash = sha256(str.encode(''.join(lst))).hexdigest()
    sort = [x for x in hash if x.isalpha()] + [x for x in hash if x.isdigit()] 
    return sha256(str.encode(''.join(sort))).hexdigest()

