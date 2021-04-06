
class Employee:
    def __init__(self, full_name, **kwargs):
        self.firstname = full_name.split()[0]
        self.lastname = full_name.split()[1]
        for k, v in kwargs.items():
            if k == 'salary':
                self.salary = v
            elif k == 'height':
                self.height = v
            elif k == 'nationality':
                self.nationality = v
            elif k == 'subordinates':
                self.subordinates = v

