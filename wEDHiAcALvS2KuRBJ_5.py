
instruction_dict = {"+": "s = sum(self.stack[-2:])\ndel self.stack[-2:]\nself.stack.append(s)",
                    "-": "s = [self.stack[-1], self.stack[-2]]\ndel self.stack[-2:]\nself.stack.append(max(s) - min(s))",
                    "*": "s = self.stack[-1] * self.stack[-2]\ndel self.stack[-2:]\nself.stack.append(s)",
                    "/": "s = [self.stack[-1], self.stack[-2]]\ndel self.stack[-2:]\nself.stack.append(max(s) // min(s))",
                    "DUP": "s = self.stack[-1]\nself.stack.insert(-1, s)",
                    "POP": "del self.stack[-1]"}
​
class StackCalc:
    def __init__(self):
        self.stack = []
        self.exception = ""
​
    def run(self, instruction):
        instruction = instruction.split()
​
        if instruction:
            if len(instruction) == 1 and instruction[0].isdigit():
                self.stack.append(int(instruction[0]))
                return
​
            for i in instruction:
                if i.isdigit():
                    self.stack.append(int(i))
                elif i in instruction_dict.keys():
                    exec(instruction_dict[i])
                else:
                    self.stack = []
                    self.exception = "Invalid instruction: {}".format(i)
                    break
​
    def getValue(self):
        if self.exception:
            return self.exception
        elif self.stack:
            return self.stack[-1]
        else:
            return 0

