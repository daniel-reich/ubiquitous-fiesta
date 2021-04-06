
class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark
​
​
class Student:
    def __init__(self, tests_taken='No tests taken'):
        self.tests_taken = tests_taken
​
    def take_test(self, paper, student_ans):
        markscheme_dict = to_dict(list(paper.markscheme))
        student_ans_dict = to_dict(list(student_ans))
        subject, result = calc_report(student_ans_dict, markscheme_dict, paper.pass_mark, paper.subject)
        if self.tests_taken == 'No tests taken':
            self.tests_taken = {subject: result}
        else:
            self.tests_taken.update({subject: result})
​
​
def calc_report(student_ans_dict, markscheme_dict, pass_mark, subject):
    right = 0
    wrong = 0
    for i in student_ans_dict.keys():
        if student_ans_dict[i] == markscheme_dict[i]:
            right += 1
        else:
            wrong += 1
    percent = int(round((right / (len(markscheme_dict)) * 100), 0))
    int_pass_mark = int(pass_mark[:-1])
    if percent >= int_pass_mark:
        status = 'Passed!'
    else:
        status = 'Failed!'
​
    percent_str = '({}%)'.format(str(percent))
    result = '{} {}'.format(status, percent_str)
    return subject, result
​
​
def to_dict(ls):
    # ls = ['1A', '2B', '3A', '4C', '5A', '6C', '7A', '8C', '9D', '10A', '11A']
    d = {}
    for item in ls:
        ques = item[0:len(item) - 1]
        ans = item[-1]
        d[ques] = ans
    return d

