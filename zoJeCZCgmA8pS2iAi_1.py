
calls = lambda x: calls(x()) + 1 if callable(x) else 0
func_sort = lambda l: sorted(l, key = calls)

