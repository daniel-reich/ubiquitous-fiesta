
def verbify(n):
     return n.split( )[0]+'d'+' '+ n.split( )[1] if n.split( )[0].endswith('e') else n.split( )[0]+' '+ n.split( )[1] if n.split( )[0].endswith('ed') else n.split( )[0]+'ed'+' '+ n.split( )[1]

