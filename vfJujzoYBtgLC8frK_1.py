
word_to_decimal=lambda w,a='abcdefghijklmnopqrstuvwxyz':sum((a.find(max(w.lower()))+11)**i*(a.find(x)+10)for i,x in enumerate(w[::-1].lower()))

