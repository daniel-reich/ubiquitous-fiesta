
invert = lambda x: ''.join(l.lower() if l.isupper() else l.upper()
                    for l in x[::-1])

