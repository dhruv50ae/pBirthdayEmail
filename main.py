import smtplib

# Let it be known that this is a disposable email, you can log in with the given creds if you're quick enough
myEmail = "andrew.thatcher.50ae@gmail.com"
myPassword = "4qv(KC3bxn6*u("

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myEmail, password=myPassword)
    connection.sendmail(from_addr=myEmail, to_addrs="andrew.thatcher.49ae@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of the email")
