from datetime import datetime
import pandas
import random
import smtplib

MYEMAIL = 'andrew.thatcher.50ae@gmail.com'
MYPASSWORD = "4qv(KC3bxn6*u("

today = datetime.now()
todayTuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdaysDict = {(dataRow.month, dataRow.day): dataRow for (index, dataRow) in data.iterrows()}

if todayTuple in birthdaysDict:
    birthdayPerson = birthdaysDict[todayTuple]
    filePath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filePath) as letterFile:
        contents = letterFile.read()
        contents.replace("[NAME]", birthdayPerson["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MYEMAIL, MYPASSWORD)
        connection.sendmail(from_addr=MYEMAIL, to_addrs=birthdayPerson["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
