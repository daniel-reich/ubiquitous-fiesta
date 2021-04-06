
class Testpaper:
    
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
    
    tests_taken = 'No tests taken'
    
    def take_test(self, paper, choices):
        score = len(set(paper.markscheme) & set(choices))/len(paper.markscheme)
        result = 'Passed!' if score >= int(paper.pass_mark[:-1])/100 else 'Failed!'
        percent = '{:.0%}'.format(score)
        
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {paper.subject: '{} ({})'.format(result, percent)}
        else:
            self.tests_taken[paper.subject] = '{} ({})'.format(result, percent)

