
hamming_code = lambda m: "".join(map(lambda x: 3*x,"".join(map(lambda x: bin(ord(x)).replace("0b","").zfill(8),m))))

