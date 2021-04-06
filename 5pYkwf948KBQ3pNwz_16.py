
def most_common_words(text,n): 
  data=text.lower().replace('\n',' ').replace("'",' ').replace(',',' ').replace('.',' ').replace('?',' ').split(' ')
  out,fst={},{}
  for x in data:
    if x!='':
      if x not in out: out[x]=0;fst[x]=len(fst)
      out[x]+=1
  return {x:out[x] for x in sorted(out.keys(),key=lambda x:(-out[x],fst[x]) )[:n] }

