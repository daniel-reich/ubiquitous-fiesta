
is_special_array = lambda x: all(i&1 == v&1 for i, v in enumerate(x))

