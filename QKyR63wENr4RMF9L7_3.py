
tweak_letters=lambda t,l:''.join('zabcdefghijklmnopqrstuvwxyza'[ord(x)+l[i]-96]for i,x in enumerate(t))

