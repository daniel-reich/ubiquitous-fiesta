
class Testpaper:
​
    def __init__(self,subject,markscheme,pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
    tests_taken = 'No tests taken'
​
    def take_test(self,name,answers):
        
        c = 0
        for i in range(len(name.markscheme)):
            if name.markscheme[i] == answers[i]:
                c += 1
        
        result = c / len(name.markscheme)
        
        if result > int (name.pass_mark[:-1]) / 100 :
            resultstr = 'Passed! '
        else:
            resultstr = 'Failed! '
        
        #tests_taken[name.subject] = f'{resultstr} {int (round(result * 100,0))}%'
        #self.tests_taken[name.subject] = '{}({}%)'.format(resultstr,int (round(result * 100,0)))
        try :
            self.tests_taken.update({name.subject : '{}({}%)'.format(resultstr,int (round(result * 100,0)))})
        except :
            self.tests_taken = {name.subject : '{}({}%)'.format(resultstr,int (round(result * 100,0)))}
​
        return self.tests_taken

