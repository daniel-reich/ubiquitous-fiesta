
def digital_decipher(msg, k):
  return ''.join([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][msg[x]-int([x for x in str(k)][x%len([x for x in str(k)])])-1] for x in range(len(msg))])

