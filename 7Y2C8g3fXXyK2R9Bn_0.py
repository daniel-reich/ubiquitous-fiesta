
keyword_cipher=lambda k,m,a='abcdefghijklmnopqrstuvwxyz':''.join((x,''.join(sorted(set(k+a),key=(k+a).find))[a.find(x)])[x in a]for x in m)

