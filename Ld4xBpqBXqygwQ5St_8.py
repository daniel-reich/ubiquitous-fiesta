
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
class Student:  
    def __init__(self, taken='No tests taken'):
        self.tests_taken = taken
    
    def take_test(self, TestPaper, answers):
        if type(self.tests_taken) == str:
            self.tests_taken = {}
        cor_ans = [i for i, j in zip(TestPaper.markscheme, answers) if i == j]
        perc_ans = round(len(cor_ans)/len(TestPaper.markscheme)*100)
        perc_mark = TestPaper.pass_mark.replace('%','')
        
        if int(perc_ans) >= int(perc_mark):
            self.tests_taken.update({TestPaper.subject:"Passed! ({d}%)".format(d=int(perc_ans))}) 
        else:
            self.tests_taken.update({TestPaper.subject:"Failed! ({d}%)".format(d=int(perc_ans))})

