
class StackCalc:
​
    def __init__(self):
        self.tmpInstruction = list()
        self.do = True
​
    def run(self, instructions):
        if instructions == "" or instructions == []:
            self.do = False
            self.tmpInstruction = 0
            return 0
        if type(instructions) == str:
            self.tmpInstruction = [item for item in instructions.split(" ")]
​
        for item in self.tmpInstruction:
            if item == "x":
                abort = "x"
                return('Invalid instruction: {}'.format(abort))
            else:
                if item == "y":
                    abort = "y"
                    return('Invalid instruction: {}'.format(abort))
        if len(self.tmpInstruction) == 1 or all(item.isdigit() for item in self.tmpInstruction):
            self.getValue()
        else:
            while self.do == True:
                for i in range(len(self.tmpInstruction)):
                    if self.do == False:
                        break
                    if self.tmpInstruction[i].isnumeric():
                        pass
                    elif self.tmpInstruction[i] == "+":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) + int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "-":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) - int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "*":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) * int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "/":
                        self.tmpInstruction[i] = str(int(self.tmpInstruction[i-1]) // int(self.tmpInstruction[i-2]))
                        del self.tmpInstruction[i-2:i]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "DUP":
                        self.tmpInstruction.insert(i-1,self.tmpInstruction[i-1])
                        del self.tmpInstruction[i+1]
                        self.run(self.tmpInstruction)
                    elif self.tmpInstruction[i] == "POP":
                        del self.tmpInstruction[i-1:i+1]
                        self.run(self.tmpInstruction)
                               
                           
            
    
    def getValue(self):
        self.do = False
        if self.tmpInstruction == 0:
            return 0
        for item in self.tmpInstruction:
            if item == "x":
                abort = "x"
                return('Invalid instruction: {}'.format(abort))
            else:
                if item == "y":
                    abort = "y"
                    return('Invalid instruction: {}'.format(abort))
        if self.tmpInstruction[-1].isdigit():
            return(int(self.tmpInstruction[-1]))
        else:
            return(self.tmpInstruction[-1])

