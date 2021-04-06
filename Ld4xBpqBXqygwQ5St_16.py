
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
    def __init__(self, tests_taken="No tests taken"):
        self.tests_taken = tests_taken
​
    def take_test(self, test: Testpaper, answers):
        correct_answers = 0
        for i in range(len(answers)):
            if test.markscheme[i] == answers[i]:
                correct_answers += 1
        percentage = round((correct_answers * 100) / len(test.markscheme))
        if percentage >= int(test.pass_mark.strip("%")):
            passed = {test.subject: "Passed! (" + str(percentage) + "%)"}
            if type(self.tests_taken) == str:
                self.tests_taken = passed
            else:
                self.tests_taken.update(passed)
        else:
            failed = {test.subject: "Failed! (" + str(percentage) + "%)"}
            if type(self.tests_taken) == str:
                self.tests_taken = failed
            else:
                self.tests_taken.update(failed)

