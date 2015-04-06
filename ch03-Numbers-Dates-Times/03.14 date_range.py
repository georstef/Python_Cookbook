from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    # find days of the given month
    help_var, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    # end_date = first day of next month
    end_date = start_date + timedelta(days=days_in_month)
    # end_date2 = last day of this month
    end_date2 = start_date + timedelta(days=days_in_month-1)
    return (start_date, end_date2)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day <= last_day:
    print(first_day)
    first_day += a_day

print('-------------------')

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

# from now to 5 days laters step by 12 hours
for d in date_range(datetime.today().replace(hour=0, minute=0, second=0,microsecond=0), datetime.today()+timedelta(days=5), timedelta(hours=12)):
    print(d)
