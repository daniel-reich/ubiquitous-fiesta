
def face_interval(num):
        try:
            if (max(num) - min(num)) in num:
                return ":)"
            else:
                return ":("
        except (ValueError, TypeError):
            return ":/"

