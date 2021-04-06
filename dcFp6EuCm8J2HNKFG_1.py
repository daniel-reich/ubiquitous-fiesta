
func = lambda lst: 0 if not type(lst) == type(list()) else sum(func(i) for i in lst) + len(lst)

