
to_snake_case=lambda s:"".join([c,"_"+c.lower()][c.isupper()]for c in s)
to_camel_case=lambda s:s[0]+"".join([b*(b!="_"),b.upper()][a=="_"]for a,b in zip(s,s[1:]))

