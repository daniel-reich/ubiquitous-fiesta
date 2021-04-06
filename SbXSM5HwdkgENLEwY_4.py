
class Selfie:
​
    def __init__(self):
        self.lst_state = []
​
    def save_state(self):
        self.lst_state.append(bytes(str(self.__dict__), 'utf-8'))
​
    def recover_state(self, n):
        if n < 0 or n >= len(self.lst_state):
            n = len(self.lst_state) - 1
        s = Selfie()
        s.__dict__ = eval(self.lst_state[n])
        s.__dict__.update({'lst_state': self.lst_state.copy()})
        return s
​
    def n_states(self):
        return len(self.lst_state)

