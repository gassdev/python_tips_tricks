import datetime
import pytz

dt_now = datetime.datetime.now()
dt_new_york = dt_now.astimezone(pytz.timezone('America/New_York'))

print(dt_now)
print(dt_new_york)
