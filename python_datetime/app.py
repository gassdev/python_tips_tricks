import datetime

tday = datetime.date.today()
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

# print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2022, 9, 20)

till_bday = bday - tday
print(till_bday)