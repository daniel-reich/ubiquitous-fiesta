
def bifid(text):
  if " " in text:
    x = polybius(text)
    x = "".join([x[y] for y in range(0, len(x), 2)] + [x[y] for y in range(1, len(x), 2)])
    return (polybius(x))
  else:
    x = (polybius(text))
    left, right = x[:len(x)//2],  x[len(x)//2:]
    x = "".join([left[y] + right[y] for y in range(len(left))])
    return (polybius(x))
  
def polybius(text):
    coords = [str(i) + str(j) for i in range(1, 6) for j in range(1, 6)]
    encrypt = dict(zip('abcdefghiklmnopqrstuvwxyz', coords))
    decrypt = dict(zip(coords, 'abcdefghiklmnopqrstuvwxyz'))
    
    if text[0].isalpha():
        text = ''.join(i for i in text.lower() if i.isalpha())
        return text.replace('j', 'i').translate(str.maketrans(encrypt))
    else:
        res = []
        for word in text.split():
            res.append(''.join(decrypt[word[i:i+2]] for i in range(0, len(word), 2)))
        return ''.join(res)

