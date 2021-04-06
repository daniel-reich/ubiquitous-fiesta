
space_message = lambda  s: s if '[' not in s else space_message(__import__('re').sub(r"\[(\d+)(\w+)\]", lambda x: x.group(2) * int(x.group(1)), s))

