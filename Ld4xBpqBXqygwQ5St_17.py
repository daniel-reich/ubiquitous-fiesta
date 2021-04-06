
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'
        self.grades = {}
​
    def take_test(self, testpaper, answers):
        markscheme = testpaper.markscheme
        pass_mark = int(testpaper.pass_mark[:-1])
        points = 0
        for n,mark in enumerate(answers):
            if markscheme[n] is mark:
                points += 100/len(answers)
        if points >= pass_mark:
            result = 'Passed! ({0}%)'.format(round(points))
        else:
            result = 'Failed! ({0}%)'.format(round(points))
        
        self.grades[testpaper.subject] = result
        self.tests_taken = self.grades

