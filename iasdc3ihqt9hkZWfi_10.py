
def can_give_blood(donor, receiver):
    return receiver in {
        'O-': ('O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'),
        'O+': ('O+', 'A+', 'B+'),
        'A+': ('A+', 'AB-'),
        'A-': ('A-', 'AB+', 'AB-'),
        'B+': ('B+', 'AB+'),
        'B-': ('B-', 'AB-'),
        'AB+': ('AB+',),
        'AB-': ('AB-',),
    }[donor]

