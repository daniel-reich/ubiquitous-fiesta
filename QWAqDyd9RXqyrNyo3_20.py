
def abbreviate(sentence, n=4):
    a=""
    for i in sentence.split():
          if len(i)>=n:
              a=a+i[0].upper()
    return a

