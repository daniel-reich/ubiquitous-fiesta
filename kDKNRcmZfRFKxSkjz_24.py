
unmix=lambda s:"".join([s[min(i+1,len(s)-1)],s[i-1]][i%2]for i in range(len(s)))

