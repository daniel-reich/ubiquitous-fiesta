
class Testpaper:
    def __init__(self,subject,markscheme,pass_mark):
        self.subject=subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark
        
class Student:
    def __init__(self,tests_taken="No tests taken"):
        self.tests_taken=tests_taken
    def take_test(self,paper,student_ans):
        if type(self.tests_taken)==str:
            self.tests_taken={}
        score=(list(i==j  for i,j in zip(paper.markscheme,student_ans)).count(True))*100/len(student_ans)
        if score>float(paper.pass_mark.replace("%","")):
            result="Passed! ({}%)".format(round(score))
        else:
            result="Failed! ({}%)".format(round(score))
        self.tests_taken[paper.subject]=result

