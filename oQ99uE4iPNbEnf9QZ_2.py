
no_perms = lambda n: 1 if n in [0, 1] else n * no_perms(n - 1)
no_perms_digits = lambda n: len(str(no_perms(n)))

