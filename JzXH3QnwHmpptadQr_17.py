
def bitwise_logical_negation(x):
  return ~((x&1)|((x>>1)&1)|((x>>2)&1)|((x>>3)&1)|((x>>4)&1)|((x>>5)&1)|((x>>6)&1)|((x>>7)&1)|((x>>8)&1))&1

