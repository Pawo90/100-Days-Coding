import smtplib as smtp
import datetime as dt
import random


MY_EMAIL = "pl.pawel.pieta@gmail.com"
# Password generated for application in security section in email provider
MY_PASSWORD = "kaerbstuviwofbdm"

DAYS_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# # Create new connection and location of smtp server
# connection = smtp.SMTP("smtp.gmail.com")
# # TLS - Transfer layer security
# connection.starttls()
# connection.login(user=my_email, password=password)
# # Correct msg for sendmail
# # msg = "Subject: Subject text\n\nContent"
#
# connection.sendmail(from_addr=my_email,
#                     to_addrs="pawelp1990@gmail.com",
#                     msg="Subject: Test\n\nMycontetnt")
# connection.close()


def send_email(address, subject, content):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=address,
                            msg=f"Subject: {subject}\n\n{content}")


def select_quote():

    with open("quotes.txt", "r") as quote:
        quote_list = quote.readlines()
    quote = random.choice(quote_list)
    return quote


date = dt.datetime.now()
year = date.year
month = date.month
day = date.day
hour = date.hour
weekday = date.weekday()

date_of_birth = dt.datetime(year=1990, month=5, day=15)
print(f"Year: {year}, Month: {month}, Day: {day}")

# if weekday == 6:
#     send_email("pawelp1990@gmail.com", f"{DAYS_NAMES[weekday]} Motivation", select_quote())
