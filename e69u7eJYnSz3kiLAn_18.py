
import hashlib
def hash_ops(n):
    listt = list(hashlib.sha256(''.join(n).encode('utf-8')).hexdigest())
​
    sorted_lisst  =sorted(listt, key=str.isdigit )
​
    hashSort = hashlib.sha256(''.join(sorted_lisst).encode('utf-8')).hexdigest()
​
    return hashSort

