
generation = lambda g,i: ['me!','','grand','great grand'][abs(g)]+['','mother','father','daughter','son'][(1+bool(ord(i)%51)+(g>0)*2)*(g!=0)]

