
fib_str = lambda n, txt: ", ".join(txt) if n<=len(txt) else fib_str(n, txt + [txt[-1] + txt[-2]])

