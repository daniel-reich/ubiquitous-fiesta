
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken
​
    def take_test(self, paper, answers):
        cor = [a[-1] for a in paper.markscheme]
        ans = [a[-1] for a in answers]
        right = sum([1 for i in range(len(cor)) if cor[i] == ans[i]])
        pct = round(100 * right / len(cor))
        if int(paper.pass_mark[:-1]) > pct:
            pf = 'Failed! '
        else:
            pf = 'Passed! '       
        if type(self.tests_taken) is str:
            self.tests_taken = {}
        self.tests_taken[paper.subject] = pf + '(' + str(pct) + '%)'

