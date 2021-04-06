
import hashlib
def hash_ops(lst):
    hash1 = ''
    for i in lst:
        hash1 += i
    hash1 = hashlib.sha256(hash1.encode()).hexdigest()
    hashsort = ''
    for i in hash1:
        if i.isalpha():
            hashsort += i
    for i in hash1:
        if not i.isalpha():
            hashsort += i
    return hashlib.sha256(hashsort.encode()).hexdigest()

