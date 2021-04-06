
def sun_loungers(beach):
  
  class Beach:
    class Space:
      
      def __init__(self, place, maxplace, lounger = False):
        self.p = place
        self.near = []
        if self.p != 0:
          self.near.append(place-1)
        if self.p != maxplace:
          self.near.append(place+1)
        self.lounger = lounger
      
      def is_possible(self, places):
        if self.lounger == True:
          return False
        for place in self.near:
          if places[place].lounger == True:
            return False
        return True
      
      def make_lounger(self):
        self.lounger = True
        return True
    
    def __init__(self, beach):
      
      self.beach = beach
      self.spaces = {}
      self.olc = 0
      
      for n in range(len(beach)):
        self.spaces[n] = Beach.Space(n, len(beach) - 1, beach[n] == '1')
        if beach[n] == '1':
          self.olc += 1
    
    def max_out_loungers(self):
      
      for n in range(len(self.beach)):
        place = self.spaces[n]
        if place.is_possible(self.spaces) == True:
          place.make_lounger()
      return True
    
    def count_loungers(self):
      count = 0
      for place in self.spaces.values():
        if place.lounger == True:
          count += 1
      return count
  
  beach = Beach(beach)
  #print(beach.olc)
  beach.max_out_loungers()
  #print(beach.count_loungers(), beach.olc)
  return beach.count_loungers() - beach.olc

