import datetime as dt
import pandas as pd
import random
import smtplib


def send_letter():
    global birthday_celebrant
    number = random.randint(1, 3)
    letter = f"letter_{number}.txt"
    with open(f"letter_templates/{letter}", "r") as message:
        message = message.read()
    message = message.replace("[NAME]", birthday_celebrant)
    with open(f"main_letter.txt", "w") as file:
        letter = file.write(message)


now = dt.datetime.now()
day = now.weekday()
month = now.month
present = f"{day}.{month}"

bt = pd.read_csv("birthdays.csv")
bt = bt.to_dict(orient='records')
for _ in bt:
    day = (_['day'])
    month = (_['month'])
    name = (_['name'])
    birthday = f"{day}.{month}"
    if birthday == present:
        birthday_celebrant = (_['name'])
        birthday_gmail = (_['email'])
        send_letter()
        my_email = "Input_your_email_here"
        password = 'input_your_password_here'
        with open("main_letter.txt", "r") as main_letter:
            main_letter = main_letter.read()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_gmail,
                                msg=f"Subject:Happy Birthday from korede\n\n {main_letter}")

# this code runs on the cloud now so until it is your birthday you will see it.
# check python anywhere website > Tasks for more information.
# you can add other people's birthday to the birthday.csv file and other letters to the letter.csv file.
