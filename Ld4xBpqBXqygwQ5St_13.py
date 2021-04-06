
class Testpaper:
    
    def __init__(self,subject,markscheme,pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
        
        
    
class Student(Testpaper):
    
    def __init__(self,tests_taken='No tests taken'):
        self.tests_taken = tests_taken
        
    def take_test(self,paper,res):
        ans = paper.markscheme
        count = 0
        passing_marks = int(paper.pass_mark[:-1])
        mydict = {}
        for i in range(len(ans)):
            if res[i] == ans[i]:
                count+=1
        percentage = round((count/len(ans))*100)
        if percentage <passing_marks:
            dic={}
            dic[paper.subject] = 'Failed!'+" ("+str(percentage)+"%)"
            mydict.update(dic)
            print(mydict)
            
        else:
            dic={}
            dic[paper.subject] = 'Passed!'+" ("+str(percentage)+"%)"
            mydict.update(dic)
            print(mydict)
            
        if type(self.tests_taken) == dict:
            self.tests_taken.update(mydict)
        else:
            self.tests_taken = mydict

