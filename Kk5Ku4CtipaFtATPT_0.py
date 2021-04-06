
coconut_translator=lambda s,c='coconuts':' '.join(''.join((c[i],c[i].upper())[k=='1']for i,k in enumerate(bin(ord(x))[2:].zfill(8)))for x in s)

