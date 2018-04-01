from datetime import datetime
from datetime import date

print("Today's Datetime - ", datetime.today())
#datetime.datetime(2018, 2, 19, 14, 38, 52, 133483)

today = datetime.today()


print("Type of datetime.today() - ", type(today))
#<class 'datetime.datetime'>


todaydate = date.today()

print("date.today() - ", todaydate)
#datetime.date(2018, 2, 19)

print("Type of date.today() - ", type(todaydate))
#<class 'datetime.date'>

print("date.today().month - ", todaydate.month)
#2

print("date.today().year - ", todaydate.year)
#2018

print("date.today().day - ", todaydate.day)
#19


christmas = date(2018, 12, 25)
print("Christmas is on : ", christmas)
#datetime.date(2018, 12, 25)

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Christmas!")