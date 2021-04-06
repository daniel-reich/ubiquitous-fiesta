
class StackCalc:
    def __init__(self):
        self.stack = []
        self.err = ""
​
​
    def run(self, instructions):
        listInstruction = []
        if instructions == '':
            self.stack.append(0)
            return self.stack
        elif instructions[0].isdigit() == False and instructions[0] != '':
            self.err = 'Invalid instruction: ' + str(instructions[0])
            return self.err
​
        for val in instructions.split():
            if val.isdigit():
                self.stack.append(int(val))
                continue
            else:
                listInstruction = instructions[instructions.index(val):].split()
                break
​
        if len(listInstruction) == 0:
            return self.stack
        
        for i in listInstruction:
            # print(i, self.stack)
            if i == "DUP":
                self.stack.append(self.stack[-1])
                continue
            elif i == "POP":
                self.stack = self.stack[:-1] if len(self.stack)>1 else [0]
                continue
            elif i.isdigit():
                self.stack.append(int(i))
                continue
            elif i.isalpha():
                self.err = 'Invalid instruction: ' + i
                return self.err
            elif eval(str(self.stack[-1]) + i + str(self.stack[-2])) == 0:
                del self.stack[-1]
                continue
            else:
                self.stack[-1] = int(eval(str(self.stack[-1]) + i + str(self.stack[-2])))
                del self.stack[-2] 
        return self.stack
    def getValue(self):
        toreturn = self.err if len(self.err)> 0 else self.stack[-1]
        return toreturn

