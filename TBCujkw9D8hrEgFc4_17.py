
def validate_email(txt):
​
    if "@" in txt:
​
        if "." in txt:
​
            if txt.index("@") != 0:
​
                if txt.rindex(".") > txt.index("@"):
​
                    if txt.rindex(".") < txt.index("com"):
​
                        return True
​
    return False

