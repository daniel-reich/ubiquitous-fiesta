
def alpha_range(a,b,s=1):
  if s and -26<s<26:
    a,b=ord(a),ord(b)
    if 64<a<91and 64<b<91or 96<a<123and 96<b<123:
      A,B=min(a,b),max(a,b)
      return list(map(chr,(range(B,A-1,s),range(A,B+1,s))[s>0]))
    else:return'both start and stop must share the same case'
  return'step must be a non-zero value between -26 and 26, exclusive'

