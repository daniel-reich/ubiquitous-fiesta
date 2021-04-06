
class Testpaper:
    subject = None
    markscheme = None
    pass_mark = None
    def __init__(self,sub,mark,pass_mark):
        self.subject = sub
        self.markscheme=mark
        self.pass_mark=pass_mark
​
class Student:
    tests_taken = None
    def __init__(self):
        self.tests_taken = 'No tests taken'
    def take_test(self, test, answers):
        fullscore = len(test.markscheme)
        resultat = 0
        for x,y in enumerate(answers):
            if test.markscheme[x] == y:
                resultat+=1
        score='{}%'.format(round((resultat / fullscore)*100),0)
        if type(self.tests_taken) == str:
            self.tests_taken={}
        if score > test.pass_mark:
            self.tests_taken[test.subject] = 'Passed! ({})'.format(score)
        else:
            self.tests_taken[test.subject] = 'Failed! ({})'.format(score)

