import datetime

# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)


dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

# print(t.date().weekday())

tdelta = datetime.timedelta(hours=12)

print(dt + tdelta)

