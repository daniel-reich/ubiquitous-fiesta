
hangman=lambda s,l:''.join((x,'-')[x.isalpha()and x.lower()not in l]for x in s)

