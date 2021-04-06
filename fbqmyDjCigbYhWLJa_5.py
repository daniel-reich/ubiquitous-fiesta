
def split_into_buckets(phrase, n):
  words = phrase.split(" ")
  idx, r = 0, [ ]
  while idx < len( words ) :
      s, j = words[ idx ], 1 
      if len( s ) > n :
          return []
      while len( s ) < n and idx + j < len( words ) :
          if len( s + " " + words[ idx + j ] ) > n :
              break
          s = s + " " + words[ idx + j ]
          j += 1
      r.append( s )
      idx += j 
  return r
​
​
​
​
  words = phrase.split(" ")
  idx = 0
  r = [ ]
  while idx < len(words) :
    if len( words[ idx ] ) > n :
      return []
    s = words[idx]
    j = 1
    while len( s ) < n :
      if len( s + " " + words[ idx + j ] ) <= n :
        s = s + " " + words[ idx + j ]
        j = j + 1
    r.append( s )
    idx = idx + j 
  return r

