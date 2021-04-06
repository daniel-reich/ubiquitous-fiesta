
import datetime
days_until_2021 = lambda date : "{} day".format((datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days) if (datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days == 1 else "{} days".format((datetime.date(2021, 1, 1) - datetime.datetime.strptime(date, '%m/%d/%Y').date()).days)

