    from email.message import EmailMessage
import ssl
import smtplib
import pandas
import datetime
from random import randint

MY_EMAIL = "esonaliyev77777@gmail.com"
MY_PASSWORD = "tvzjucdnvdvbzpsd"
# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = {row.nama: {"email": row.email, "year": row.year, "month": row.month, "day": row.day, } for (index, row)
             in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
month = now.month
day = now.day
for person in data_dict:
    birthday_month = data_dict[person]["month"]
    birthday_day = data_dict[person]["day"]
    email = data_dict[person]["email"]
    if month == birthday_month and day == birthday_day:
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as file:
            content = file.read()
            new_file = content.replace("[NAME]", person)
            subject = f"Happy Birthday, {person}"
            body = new_file
            em = EmailMessage()
            em["From"] = MY_EMAIL
            em["To"] = email
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(MY_EMAIL, MY_PASSWORD)
                smtp.sendmail(MY_EMAIL, email, em.as_string())
