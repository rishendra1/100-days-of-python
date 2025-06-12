import datetime
import smtplib
now = datetime.datetime.now()
year = now.year
day = now.day
month = now.month
print(now)
user_Name = input("What is your name? ")
user_day = int(input("Enter your day of birthday : "))
user_month = int(input("Enter your month of birthday : "))
user_year = int(input("Enter your year of birthday : "))

my_mail = "<EMAIL>"
password = "<PASSWORD>"
if day == user_day and month == user_month :
    Age = year - user_year
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs=my_mail,
        message = f"Subject: B'Day Wishes\n\nDate: {now}\nHappy Birthday {user_Name}"
    )
    connection.quit()
    print("Thank You!")
else:
    print("No thanks")

