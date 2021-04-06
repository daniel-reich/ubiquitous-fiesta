
class Spartan:
  
  def __init__(self, slides):
    self.slides = slides
  
  def encode(self, msg):
    if msg == '':
      return msg
    slide_size = len(msg) // self.slides if len(msg) % self.slides == 0 else len(msg) // self.slides + 1
    
    slides = [[] for slide in range(slide_size)]
    #print(slides, 'slides')
    for n in range(len(msg)):
      try:
        slides[n].append(msg[n])
      except IndexError:
        #print(slides, n, slide_size, n%slide_size)
        slides[n%slide_size].append(msg[n])
    
    slides = [''.join(slide) for slide in slides]
    ns = []
    for slide in slides:
      #print(slide, len(slide), self.slides)
      while len(slide) < self.slides:
        slide += ' '
        #print(slide, len(slide), 'L.24')
      ns.append(slide)
    
    
    tr = ''.join(ns)
    
    while tr[0] == ' ':
      tr = tr[1:]
    while tr[-1] == ' ':
      tr = tr[:-1]
    
    return tr
    
def spartans_cipher(message, n_Slide):
  
  msg = Spartan(n_Slide)
  m = msg.encode(message)
  
  return m

