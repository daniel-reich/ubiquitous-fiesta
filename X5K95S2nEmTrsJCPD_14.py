
def emotify(txt):
 dic ={"smile":":D", "grin":":)", "sad":":(", "mad":":P"}
 return txt[:8] + dic[txt[8:]]

