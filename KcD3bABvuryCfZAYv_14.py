
def most_frequent_char(lst):
    from collections import Counter
    cnt = dict(Counter("".join(lst)).most_common())
    max_value = max(cnt.values())
    return sorted([k for k, v in cnt.items() if v == max_value])

