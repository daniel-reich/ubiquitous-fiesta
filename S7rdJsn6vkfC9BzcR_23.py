
class Employee:
    def __init__(self, name, **kwargs):
        self.name = name.split()[0]
        self.lastname = name.split()[1]
        for arg in kwargs:
            try: exec('self.{} = {}'.format(arg, kwargs[arg]))
            except: exec('self.{} = "{}"'.format(arg, kwargs[arg]))

