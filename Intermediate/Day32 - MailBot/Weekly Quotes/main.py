import smtplib
import datetime as dt
import random

my_email = [PLACEHOLDER]
bot_email = [PLACEHOLDER]
bot_password = [PLACEHOLDER]

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=bot_email, password=bot_password)

        connection.sendmail(
            from_addr=bot_email,
            to_addrs=my_email
            msg=f"Subject:Weekly quote\n\n{quote}"
        )



