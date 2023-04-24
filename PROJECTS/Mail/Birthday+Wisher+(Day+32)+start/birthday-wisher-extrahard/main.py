##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import os
import random
import smtplib as smtp

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


MY_EMAIL = "pl.pawel.pieta@gmail.com"
MY_PASSWORD = "kaerbstuviwofbdm"

# READ TODAY DATA ----------------------------------
date = dt.datetime.now()
today_month = date.month
today_day = date.day
today = (today_month, today_day)

# print(f"Today is {today_day} of {MONTHS[today_month]}")


# READ FILE WITH BIRTHDAYS -------------------------
df = pd.read_csv("birthdays.csv")


# Check if anybody have birthday today
def check_birthday(dataframe, today):
    birthday_data = [{"name": dataframe.loc[i, "name"], "email": dataframe.loc[i, "email"]}
                     for i in range(len(dataframe))
                     if dataframe.loc[i, "month"] == today[0] and dataframe.loc[i, "day"] == today[1]
    ]
    return birthday_data


# PICK RANDOM LETTER TEMPLATE AND REPLACE NAME ----------------------------
def prepare_letter(person_name):
    # Pick random letter from letters templates
    filename = random.choice(os.listdir("./letter_templates"))
    with open(f"./letter_templates/{filename}", "r") as file:
        letter = file.read()
    # Change name in letter
    letter = letter.replace("[NAME]", person_name)

    return letter


# SEND EMAIL TO EACH PERSON ----------------------------------------------
def send_email(address, letter):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=address,
                            msg=f"Subject: Happy birthday!\n\n{letter}")


# CALLING A FUNCTIONS -------------------------------------------------
birth_data = check_birthday(df, today)

if len(birth_data) != 0:
    for i in range(len(birth_data)):
        email = birth_data[i]["email"]
        letter = prepare_letter(birth_data[i]["name"])
        print(email)
        print(letter)
        send_email(email, letter)
