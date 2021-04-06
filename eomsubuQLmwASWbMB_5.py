
def weekday_dutch(date):
    import datetime
    day_name = {"Monday": "maandag", "Tuesday": "dinsdag", "Wednesday": "woensdag", "Thursday": "donderdag",
                "Friday": "vrijdag", "Saturday": "zaterdag", "Sunday": "zondag"}
    day = datetime.datetime.strptime(date, '%d %m %Y').strftime("%A")
    return day_name[day]

