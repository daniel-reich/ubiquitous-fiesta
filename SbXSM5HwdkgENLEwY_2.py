
import pickle
class Selfie:
  def __init__(self):
    self.lst_state = []
  
  def save_state(self):
    d = {}
    for elem in self.__dict__:
      if elem != 'lst_state':
        d[elem] = self.__dict__[elem]
    self.lst_state.append(pickle.dumps(d))
​
  def recover_state(self, n):
    try:
      recovered_selfie = Selfie()
      recovered_selfie.__dict__ = pickle.loads(self.lst_state[n])
      recovered_selfie.lst_state = self.lst_state.copy()
    except:
      recovered_selfie = self
    return recovered_selfie
  
  def n_states(self):
    return len(self.lst_state)

