
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark  
​
class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"
​
    def take_test(self, clss, opts):
        p_mark = int(clss.pass_mark.rstrip("%"))
        if type(self.tests_taken) is not type(dict()):
            self.tests_taken = {}
        avg = round(sum(True for x in opts if x in clss.markscheme)/len(clss.markscheme)*100) 
        if_passed = "Passed!" if avg >= p_mark else "Failed!"
        self.tests_taken[clss.subject] = "{} ({}%)".format(if_passed, avg)

