
def sorting(s):
  ord="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
  return ''.join(sorted(s,key=lambda x: ord.index(x)))

