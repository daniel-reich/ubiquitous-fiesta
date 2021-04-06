
import re
​
class Selfie:
    def __init__(self):
        self.lst_state = []
​
    def save_state(self):
        state = str(self.__dict__)
        self.lst_state.append(b''.join(ord(s).to_bytes(2, byteorder='big') for s in state))
​
    def recover_state(self, n):
        if n < self.n_states():
            bytes = self.lst_state[n]
            meh = self.lst_state[:]
            fst = ''.join(chr(b) for b in bytes)
            self.__dict__ = eval(''.join(fst[i] for i in range(1, len(fst), 2)))
            self.__dict__['lst_state'] = meh
        return self
​
    def n_states(self):
        return len(self.lst_state)

