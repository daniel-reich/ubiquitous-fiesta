
s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2 = "22233344455566677778889999"
text_to_num = lambda s: s.translate(s.maketrans(s1,s2,''))

