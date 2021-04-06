
tweak_letters=lambda s,l:"".join(chr(97+(ord(c)+n+7)%26)for c,n in zip(s,l))

