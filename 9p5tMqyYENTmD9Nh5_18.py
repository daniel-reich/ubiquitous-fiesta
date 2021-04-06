
is_valid_hex_code=lambda t:bool(__import__("re").fullmatch("(?i)#[\da-f]{6}",t))

