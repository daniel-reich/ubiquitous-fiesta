
def format_ascii(txt, width):
    rez = ''
    for i in range(int(len(txt)/width)):
      rez = rez + txt[i*width:(width+i*width)]
      if i < int(len(txt)/width)-1: 
        rez = rez + '\n'
    return(rez)

