import pandas
import datetime as dt
import random
import smtplib



##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

def sender(destinatario, mail):
    my_email = "carlos@gmail.com"
    password = "Añadir_Password"

    connection = smtplib.SMTP("smtp.gmail.com")
    port = 587

    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=destinatario, msg=f"Subject: Happy birthday!!\n\n{mail}")
    connection.close()



now = dt.datetime.now()

birthday_list = pandas.read_csv("birthdays.csv")
birthday = birthday_list.to_dict(orient="index")


def bday():
    for x in birthday:
        year = birthday[x]["year"]
        month = birthday[x]["month"]
        day = birthday[x]["day"]
        biday = dt.date(year=year, month=month, day=day)
        birthday[x].update({"date": biday})

def check_birthday():
    #letter = random.randint(1, 3)
    for x in birthday:
        letter = random.randint(1, 3)
        if birthday[x]["date"].month == now.month and birthday[x]["date"].day == now.day:
            birthday_person = birthday[x]["name"]
            birthday_person_email = birthday[x]["email"]
            with open(f"letter_templates/letter_{letter}.txt", mode="r") as file:
                birthday_mail_raw = file.read()
                birthday_mail = birthday_mail_raw.replace("[NAME]", birthday_person)
            sender(destinatario=birthday_person_email, mail=birthday_mail)



bday()
check_birthday()






