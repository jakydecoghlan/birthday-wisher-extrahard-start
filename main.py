##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd


# 1. Update the birthdays.csv
# with open("birthdays.csv", "w") as data:
#     data.write("juanca, jakytest@gmail.com, 1990,1,27")



# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day
day_of_the_week = now.weekday()
today = (month, day)
print(today)

df = pd.read_csv("birthdays.csv", index_col=False)
birthdays = df.to_dict()
print(birthdays)
birthday_months = birthdays["month"]
print(birthday_months)
birthday_days = birthdays["day"]
print(birthday_days)
jaky = df[df.name =="jaky"]
print(jaky)

# new_dict = {(birthday_months, birthday_days): data_row for (index, data_row) in df.iterrows()}
# print(new_dict)
# #



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




