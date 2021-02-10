from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = [PLACEHOLDER]
BOT_EMAIL = [PLACEHOLDER]
BOT_PASSWORD = [PLACEHOLDER]

today = datetime.now()
today_tuple = (today.day, today.month)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["day"], data_row["month"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(BOT_EMAIL, BOT_PASSWORD)
        connection.sendmail(
            from_addr=BOT_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Birthday Reminder\n\nToday's {birthday_person}'s birthday! Don't forget to congratulate."
        )
