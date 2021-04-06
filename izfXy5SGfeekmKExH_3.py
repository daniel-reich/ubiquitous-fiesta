
puzzle_pieces=lambda a,b:len(a)==len(b)and all(x+y==a[0]+b[0]for x,y in zip(a,b))

