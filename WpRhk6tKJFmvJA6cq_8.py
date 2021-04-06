
from datetime import timedelta, datetime
def manage_delays(train, dest, delay):
    if dest in train.destinations:
        train.expected_time = datetime.strftime(datetime
                                                .strptime(train.expected_time,
                                                          '%H:%M')
                                                + timedelta(minutes=delay),
                                                '%H:%M')

