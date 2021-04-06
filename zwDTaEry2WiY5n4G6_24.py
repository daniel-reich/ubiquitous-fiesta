
ban=lambda n,b:''.join(filter(lambda u:not u in{'e':'1357890', 'i':'5689', 'o':'1240', 'u':'4'}[b], str(n)))
digital_vowel_ban=lambda n,b:(int(ban(n,b)) if ban(n,b) else "Banned Number") if b in 'eiou' else n

