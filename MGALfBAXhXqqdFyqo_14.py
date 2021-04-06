
atbash=lambda t:''.join([chr(ord(l)+25+2*(97-ord(l.lower()))) if l.isalpha() else l for l in t])

