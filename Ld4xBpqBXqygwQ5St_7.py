
class Testpaper:
​
    def __init__(self,subject,markscheme,pass_mark):
        self.subject =subject
        self.markscheme=markscheme
        self.pass_mark=pass_mark
        self.passmark=int(pass_mark.strip('%'))
        
​
class Student:
    
    def __init__(self):
        self.tests_taken = 'No tests taken'
        self.total_result={}
        self.verdict=''
        
    def take_test(self,testpaper,answers):
        i=0
        total_marks= 0
        correct_answer=0
        for answer in testpaper.markscheme:
            if answer == answers[i]:
                correct_answer+=1
            i+=1
        total_marks=round((correct_answer/i)*100)
        if total_marks >= testpaper.passmark:
            self.verdict='Passed!'
        else:
            self.verdict='Failed!'
        self.total_result[testpaper.subject]=self.verdict+ ' ('+str(total_marks)+'%)'
        self.tests_taken=self.total_result

