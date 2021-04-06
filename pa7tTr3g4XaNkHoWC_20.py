
vow = lambda x: min( i for i in range(len(x)) if x[i] in 'aeiou' )
pig = lambda x: x+'way' if not vow(x) else x[vow(x):]+x[:vow(x)]+'ay'
pig_latin_sentence = lambda t: ' '.join( pig(w) for w in t.split() )

