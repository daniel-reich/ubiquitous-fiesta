
binary_conversion=lambda s:"".join(chr(int(s[i:i+8],2))for i in range(0,len(s),8))

