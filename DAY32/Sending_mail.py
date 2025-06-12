import smtplib
#give your mail
my_email = "rishendra009@gmail.com"
password = "Rishendra009"
#create a new scratch file
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="rishendra1337@gmail.com",
    msg="Subject:Hello\n\nSodium Magnesium"
)
connection.close()