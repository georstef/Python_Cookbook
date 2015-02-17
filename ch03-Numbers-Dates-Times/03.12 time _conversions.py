from datetime import timedelta
from datetime import datetime

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b  # 2 days and 10.5 hours
print(c)
print(c.days) # 2 days
print(c.seconds/3600)  # 10.5 hours (only seconds of the hours part)
print(c.total_seconds())  # (seconds of days and hours together)

print('------')

a = datetime(2014, 12, 31)
print(a)
print(a - timedelta(days=10))  # result is datetime

print('------')

b = datetime(2014, 12, 21)
c = b - a  # 21/12/2014 - 31/12/2014 (-10 days)
print(c)  # result is timedelta

print('------')

now = datetime.today()
print(now)
print(now - timedelta(minutes=10))  # 10 minutes ago


# timedelta + timedelta = timedelta
# timedelta - timedelta = timedelta

# datetime + timedelta = datetime
# datetime - timedelta = datetime

# datetime - datetime = timedelta
