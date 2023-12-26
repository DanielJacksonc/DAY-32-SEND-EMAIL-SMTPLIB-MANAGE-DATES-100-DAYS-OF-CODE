import datetime
import random
import smtplib
import pandas as pd

##################### Normal Starting Project ######################


# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
today_tuple =(today.month, today.day)

# HINT 2: Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")


# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# data_dict = data.set_index("name").to_dict(orient="index")
# print(data_dict)

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today_tuple in birthday_dict:
    details = birthday_dict[today_tuple]
    name = details["name"]





# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter.
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp
    with open(file_path) as letters:
        the_letter = letters.read()
        new_letter = the_letter.replace('[NAME]', name)
# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "pythondanielpython@gmail.com"
    passwords = "sjrmiwoqvnxixlbi"
    # HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        # HINT 2: Remember to call .starttls()
        connection.starttls()
        # HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
        connection.login(user=my_email,password=passwords)
        # HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
        connection.sendmail(
            from_addr=my_email,
            to_addrs = details["email"],
            msg=f"Subject:Happy Birthday {name}\n\n{new_letter}")



