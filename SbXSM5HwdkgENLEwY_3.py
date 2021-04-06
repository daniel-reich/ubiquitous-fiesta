
from pickle import loads, dumps
class Selfie:
    def __init__(self):
        self.lst_state = []
    def save_state(self):
        self.lst_state.append(dumps({attr: getattr(self, attr) for \
    attr in dir(self)}))
    def recover_state(self, index):
        if index >= len(self.lst_state):
            return self
        new = Selfie()
        for attr, value in loads(self.lst_state[index]).items():
            if attr not in dir(Selfie):
                exec("new.%s = value" % attr)
        new.lst_state = self.lst_state
        return new
    def n_states(self):
        return len(self.lst_state)

