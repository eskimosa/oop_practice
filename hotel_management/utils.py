from datetime import date, timedelta


def get_weekdays_and_weekends(start_date: date, end_date: date):
    weekdays = 0
    weekends = 0

    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays += 1
        else:
            weekends += 1
        current_date += timedelta(days=1)

    return weekdays, weekends
