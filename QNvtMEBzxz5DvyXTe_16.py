
def strong_password(password):
        numbers = "0123456789"
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        special_characters = "!@#$%^&*()-+"
        se=set()
        for i in password:
                if i in numbers:
                        se.add(2)
                elif i in lower_case:
                        se.add(3)
                elif i in upper_case:
                        se.add(4)
                elif i in special_characters:
                        se.add(5)
        if len(password)+len(se)>=6:
                se.add(1)
        else:
                return 6-len(password)
        return 5-len(se)

