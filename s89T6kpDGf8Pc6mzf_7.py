
def seven_segment(txt):
  d={'0':set('abcdef'),'1':set('bc'),'2':set('abdeg'),'3':set('abcdg'),'4':set('bcfg'),'5':set('acdfg'),'6':set('acdefg'),'7':set('abc'),'8':set('abcdefg'),'9':set('abcfg')}
  res = []
  for a,b in zip(txt,txt[1:]):
    dif=d[a]^d[b];mem=[]
    for i in 'abcdefg':
      if i in dif:
        if i in d[a]:mem+=[i]
        else:mem+=[i.upper()]
    res+=[mem]
  return res

