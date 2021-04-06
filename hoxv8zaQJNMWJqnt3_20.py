
def is_heteromecic(k, s=None):
    return is_heteromecic(k, int(pow(k, 0.5))) if s is None else s * (s + 1) == k

