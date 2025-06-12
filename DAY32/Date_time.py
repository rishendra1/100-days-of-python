import datetime as dt

from sqlalchemy.sql.functions import now

date = dt.datetime.now()
print(date)
year = date.year
print(year)
month = date.month
print(month)
week = date.weekday()
print(week)
Date_of_Birth = dt.datetime(year=2006, month=2,day=18)
print(Date_of_Birth)
