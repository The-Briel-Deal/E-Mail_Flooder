import random
import smtplib
import datetime
import imghdr
import email.message

#  Mailing List

#  Credentials
my_email = "{Enter E-Mail}"
password = "{Enter Password}"

#  Creating current date object
current_date = datetime.datetime.now()

#  Initializing connection and starting TLS
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)


MESSAGE = email.message.EmailMessage()
MESSAGE['Subject'] = 'CRITICAL ALERT'
MESSAGE['From'] = 'gfapsnmpblasterbussy@gmail.com'
MESSAGE['To'] = da_bros


# MESSAGE.preamble = 'You will not see this in a MIME-aware mail reader.\n'

with open("quotes.txt", mode="r") as quotes:
    quote = quotes.readlines()[random.randint(0, 100)]
    content = str(f"IT IS HUMP DAYYY!!!!!!!!!!!!\nHere is your hump day quote:\n{quote}")

MESSAGE.set_content(content)


with open("its-wednesday-camel-.jpg", mode="rb") as file:
    read_file = file.read()
    MESSAGE.add_attachment(read_file, maintype='image', subtype=imghdr.what(None, read_file))
while True:
    print("cute dog")
    connection.send_message(MESSAGE)
connection.close()
