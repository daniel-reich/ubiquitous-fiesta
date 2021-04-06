
import collections
​
​
def mode(nums):
    n_list = collections.Counter(nums)
    max_item = max(n_list.items(), key=lambda x: x[1])
    list_of_keys = []
    for key, value in n_list.items():
        if value == max_item[1]:
            list_of_keys.append(key)
    return sorted(list_of_keys)

