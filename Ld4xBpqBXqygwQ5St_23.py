
class Testpaper:
​
    def __init__ (self, subject,markscheme,pass_mark):
        self.subject= subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark
​
class Student:
    def __init__(self):
        self.tests_taken="No tests taken"
​
    def take_test(self,obj,answers):
        if self.tests_taken=="No tests taken":
            self.tests_taken={}
        note =0
        for i in range(len(answers)):
            if answers[i]==obj.markscheme[i]:
                note+=1
        percentage=round(note/len(obj.markscheme)*100)
        if percentage >= int(obj.pass_mark[0:-1]):
            self.tests_taken[obj.subject]="Passed! "+"("+str(percentage)+"%)"
        else:
            self.tests_taken[obj.subject] = "Failed! " + "(" + str(percentage) + "%)"

