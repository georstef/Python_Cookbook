from datetime import datetime, timedelta

weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']

def get_previous_byday(dayname, start_date=None):
    if not start_date:
        start_date = datetime.today()
    day_num = start_date.weekday()  # get weekday No (monday=0)
    day_num_target = weekdays.index(dayname)  # get dayname No (sunday=7)
    days_ago = (7 + day_num - day_num_target) % 7  # get difference
    if not days_ago:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago) # find the date
    return target_date

print(datetime.today())
print(get_previous_byday('Mo'))
print(get_previous_byday('Th'))
print(get_previous_byday('Fr'))
print(get_previous_byday('Fr', get_previous_byday('Fr')))
