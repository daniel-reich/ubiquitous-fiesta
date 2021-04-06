
def can_move(piece, current, target):
  fc,ft,rc,rt = ord(current[0])-64,ord(target[0])-64,int(current[1]),int(target[1])
  if piece == 'Pawn':
    return ft == fc and (rt-rc == 1 or (rt == 4 and rc == 2))
  elif piece == 'Knight':
    return ((rt == rc+1 or rt == rc-1) and (ft == fc+2 or ft == fc-2)) or ((rt == rc+2 or rt == rc-2) and (ft == fc+1 or ft == fc-1))
  elif piece == 'Bishop':
    return (rt-rc == ft-fc) or (fc+ft == rc+rt)
  elif piece == 'Rook':
    return rt == rc or ft == fc
  elif piece == 'King':
    return fc-1 <= ft <= fc+1 and rc-1 <= rt <= rc+1
  else:
    return can_move('Bishop',current,target) or can_move('Rook',current,target)

