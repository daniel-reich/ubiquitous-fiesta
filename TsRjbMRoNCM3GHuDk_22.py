
def syllabification(word):
  consonants = ['p','b','t','d','k','g','G','?','f','v','s', 
               'z','S','Z','x','h','c','j','m','n','r','l',
               'y']
  vowels, pos, out, p1, dotcount = ['a','A','e','i','o','u'],[],'',0,0
  pos = [i for i in range (len(word)) if word[i] in vowels]
  for i in range (len(pos)):
    if (i ==  len(pos)-1):
      out+=word[p1:]
    else:
      out+=word[p1:pos[i+1]-1]+'.'
      dotcount+=1
    p1= len(out)-dotcount
  return out

