
class StackCalc:
​
    def __init__(self):
        self.s = []
        self.err = False
​
    def run(self, instructions):
        for i in instructions.split():
            if not self.err:
                if i.isdigit():
                    self.s += [int(i)]
                elif i == '+':
                    self.s += [self.s.pop() + self.s.pop()]
                elif i == '-':
                    self.s += [self.s.pop() - self.s.pop()]
                elif i == '*':
                    self.s += [self.s.pop() * self.s.pop()]
                elif i == '/':
                    self.s += [int(self.s.pop() / self.s.pop())]
                elif i == 'DUP':
                    self.s += [self.s[-1]]
                elif i == 'POP':
                    self.s.pop()
                else:
                    self.ret = 'Invalid instruction: '+i
                    self.err = True
​
    def getValue(self):
        if self.err:
            return self.ret
        if not self.s:
            return 0
        return self.s[-1]

