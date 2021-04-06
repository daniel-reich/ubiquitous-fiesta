
def can_move(piece, current, target):
  key = {"Pawn":canPawn(current,target),"Knight":canKnight(current,target),"Rook":canRook(current,target),"Bishop":canBishop(current,target),"Queen":canQueen(current,target),"King":canKing(current,target)}
  return key[piece]
  
  
  
def canPawn(current,target):
  rank1,file1,rank2,file2 = current[1],current[0],target[1],target[0]
  chk = file1 == file2
  if rank1 == '2':
    return chk and rank2 in ['3','4']
  elif rank1 == '7':
    return chk and rank2 in ['6','5']
  return chk and int(rank2)-int(rank1)==1
  
  
def canKnight(current,target):
  rank1,file1,rank2,file2 = current[1],current[0],target[1],target[0]
  files = 'ABCDEFGH'
  fileDiff = abs(files.index(file2)-files.index(file1))
  rankDiff = abs(int(rank1)-int(rank2))
  if fileDiff == 2:
    return rankDiff == 1
  elif fileDiff == 1:
    return rankDiff == 2
  return False
  
  
def canRook(current,target):
  rank1,file1,rank2,file2 = current[1],current[0],target[1],target[0]
  return rank1 == rank2 or file1 == file2
  
  
def canBishop(current,target):
  rank1,file1,rank2,file2 = current[1],current[0],target[1],target[0]
  files = 'ABCDEFGH'
  fileDiff = abs(files.index(file2)-files.index(file1))
  rankDiff = abs(int(rank1)-int(rank2))
  return fileDiff == rankDiff
  
​
def canQueen(current, target):
  return canRook(current, target) or canBishop(current, target)
​
​
def canKing(current,target):
  rank1,file1,rank2,file2 = current[1],current[0],target[1],target[0]
  files = 'ABCDEFGH'
  fileDiff = abs(files.index(file2)-files.index(file1))
  rankDiff = abs(int(rank1)-int(rank2))
  return fileDiff <= 1 and rankDiff <= 1

