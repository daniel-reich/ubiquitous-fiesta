
def elasticize(word):
 return ''.join(y*(x+1 if x< len(word)/2 else len(word)-x) for x,y in enumerate(word))

