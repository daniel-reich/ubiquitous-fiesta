
missing_letter = lambda lst:list(set([chr(n) for n in range(min([ord(n) for n in lst]),max([ord(n) for n in lst])+1)])-set(lst))[0]

