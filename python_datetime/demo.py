import datetime
import pytz

dt = datetime.datetime(2016, 7, 26, 7, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_dakar = dt_utcnow.astimezone(pytz.timezone('Africa/Dakar'))
print(dt_dakar)

# for tz in pytz.all_timezones:
#     print(tz)