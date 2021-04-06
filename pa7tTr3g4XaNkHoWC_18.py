
def pig_latin_sentence(sentence):
  a=sentence
  x=a.split(' ')
  a=a.split(' ')
  fin=''
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][0]!='a' and a[i][0]!='e' and a[i][0]!='i' and a[i][0]!='o' and a[i][0]!='o':
        if a[i][j]=='a' or a[i][j]=='e' or a[i][j]=='i'  or a[i][j]=='o'  or a[i][j]=='u':
          a[i]=a[i][j:]+a[i][:j]
          a[i]+='ay'
  for i in range(len(a)):
    if a[i]==x[i]:
      a[i]+='way'
  for i in a:
    fin+=' '+i
  return(fin[1:])

