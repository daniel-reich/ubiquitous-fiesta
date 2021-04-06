
def seating_students(lst):
​
  class Classroom:
    class Seat:
​
      def __init__(self, ident, maxid, occupied = False):
        self.id = ident
        self.occ = occupied
        self.mid = maxid
​
        self.nearby = []
​
        if self.id not in [1, 2]:
          self.nearby.append(self.id - 2)
        if self.id % 2 == 0:
          self.nearby.append(self.id - 1)
        else:
          self.nearby.append(self.id + 1)
        if self.id not in [self.mid - 1, self.mid]:
          self.nearby.append(self.id + 2)
    
    def __init__(self, num_of_seats):
      self.nos = num_of_seats
      self.seats = {}
​
      for n in range(1, self.nos + 1):
        self.seats[n] = Classroom.Seat(n,self.nos)
    
    def occupy(self, seat):
      self.seats[seat].occ = True
      return True
    
    def count_unocc_pairs(self):
      unocc_pairs = set()
      for sid in self.seats.keys():
        seat = self.seats[sid]
        if seat.occ == True:
          continue
        nearby_seats = seat.nearby
        for nsid in nearby_seats:
          if self.seats[nsid].occ == False:
            pair = ','.join(sorted([str(sid), str(nsid)]))
            unocc_pairs.add(pair)
      return len(list(unocc_pairs))
​
  classroom = Classroom(lst[0])
​
  for chair in lst[1:]:
    classroom.occupy(chair)
  
  return classroom.count_unocc_pairs()

