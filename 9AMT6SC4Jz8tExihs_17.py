
generate_nonconsecutive=lambda n:' '.join(bin(i)[2:].zfill(n)for i in range(1<<n)if'11'not in bin(i))

