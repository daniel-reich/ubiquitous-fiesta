
import hashlib
def hash_ops(lst):
    lst_hash_strings = list(hashlib.sha256(''.join(lst).encode('utf-8'))
                            .hexdigest())
    letters = [c for c in lst_hash_strings if c.isalpha()]
    digits = [c for c in lst_hash_strings if c.isdigit()]
    return hashlib.sha256(''.join(letters + digits)
                          .encode('utf-8')).hexdigest()

