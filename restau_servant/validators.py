from datetime import datetime

def valid_date(date):
    now = datetime.now()
    if datetime.strptime(date, "%Y-%m-%d") <= now:
        raise ValueError('Too late to do a reservation.')
    return date