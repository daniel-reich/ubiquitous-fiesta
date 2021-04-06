
def palindromic_date(date):
    date_to_check = date.replace("/", "")
    return date_to_check == date_to_check[::-1] and date[:2] == date[3:5]

