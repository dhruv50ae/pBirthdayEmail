import smtplib
import datetime as dt
import random

MYEMAIL = "andrew.thatcher.50ae@gmail.com"
MYPASSWORD = "4qv(KC3bxn6*u("

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as qFile:
        allQuotes = qFile.readlines()
        quote = random.choice(allQuotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL, MYPASSWORD)
        connection.sendmail(from_addr=MYEMAIL, to_addrs=MYEMAIL, msg=f"Subject: Monday Motivation\n\n{quote}")
