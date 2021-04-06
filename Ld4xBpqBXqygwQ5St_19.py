
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
class Student:
    def __init__(self):
        self.tests_taken = 'No tests taken'
​
​
​
    def take_test(self, test, marks):
        check = list(zip(test.markscheme, marks))
        answers = sum([1 if answers[0] == answers[1] else 0 for answers in check]) * 100 / len(test.markscheme)
        answers = '{}! ({}%)'.format('Passed' if answers > int(test.pass_mark[:2]) else 'Failed', round(answers))
        try:
            self.tests_taken.setdefault(test.subject, answers)
        except Exception:
            self.tests_taken = {}
            self.take_test(test, marks)

