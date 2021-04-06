
def wash_hands(N, nM):
  return (str((N * 21 * nM * 30) // 60) + ' minutes and ' + 
        str((N * 21 * nM * 30) % 60) + ' seconds')

