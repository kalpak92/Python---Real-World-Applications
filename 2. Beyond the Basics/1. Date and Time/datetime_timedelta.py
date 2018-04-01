from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

print ("timedelta(days=4, hours=10) : ", t)
print("t.days - ", t.days)
#4

print("t.seconds - ", t.seconds)
#36000

#t.hours
#Traceback (most recent call last):
    #File "<pyshell#119>", line 1, in <module> t.hours
#AttributeError: 'datetime.timedelta' object has no attribute 'hours'

print("t.seconds / 60 / 60 :", t.seconds / 60 / 60)
#10.0

print("t.seconds/3600 : ", t.seconds / 3600)
#10.0


#########
print ("\n********************")

eta = timedelta(hours=6)
print("eta : ", eta)

today = datetime.today()

print("today : ", today)
#datetime.datetime(2018, 2, 19, 14, 55, 19, 197404

print("today + eta : ", today + eta)
#datetime.datetime(2018, 2, 19, 20, 55, 19, 197404)

str(today + eta)
#'2018-02-19 20:55:19.197404'