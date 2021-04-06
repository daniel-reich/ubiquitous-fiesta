
def squares_sum(n):
    squares = []
    for i in range(n+1):
      sq = i**2
      squares.append(sq)
      
    total = sum(squares)
    return total

