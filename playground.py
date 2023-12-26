# """we want to creatw an atomated email, it will send email on a specific day"""
#
# # import all my modules, including the datetime modules and the smtplib
# import datetime
# import smtplib
# import random
#
# my_email = "pythondanielpython@gmail.com"
# passwords = "sjrmiwoqvnxixlbi"
#
#
#
# now = datetime.datetime.now()
# today = now.weekday()
# print(today)
#
# if today == 0:
#     with open("quotes.txt") as my_quotes:
#         all_quotes = my_quotes.readlines()
#         quote = random.choice(all_quotes)
#
#     with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=passwords)
#         connection.sendmail(
#             from_addr="pythondanielpython@gmail.com",
#             to_addrs="pythondanielpython@yahoo.com",
#             msg=f"Subject: daily Quotes.\n\n{quote} ")

#
# import pandas as pd
#
# names = pd.read_csv("names.csv")
# names_dict = names.to_dict()
#
# names1 = names_dict["name"]
# print(names_dict)

# import datetime
#
# full_date = datetime.datetime.now()
# now = full_date.date()
# today = now.day
# print(now)
# print(today)




