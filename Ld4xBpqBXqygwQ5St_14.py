
class Testpaper:
​
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
​
    
    def __init__(self):
        
        self.tests_taken = 'No tests taken'
        self.count = 0
        
    def take_test(self, Testpaper, answers):
​
        if self.count == 0:
            self.count += 1
            self.tests_taken = {}
        
        test = {}
        score = 0
        pass_mark = int(Testpaper.pass_mark[:-1])
        for a in range(len(answers)):
            if answers[a] == Testpaper.markscheme[a]:
                score += 1
        grade = round(score / len(Testpaper.markscheme) * 100)
        if grade >= pass_mark:
            grade = "Passed! (" + str(grade) + "%)"
        else:
            grade = "Failed! (" + str(grade) + "%)"
​
        self.tests_taken[Testpaper.subject] = grade

