#classmethod
class Pizza():
    
    def __init__(self, ingridiens):
        self.ingridiens = ingridiens
    
    def __repr__(self):
        return f'pizza ({self.ingridiens})'

    @classmethod
    def margarita(cls):
        return cls ('chees, tomatoes')

    @classmethod
    def prosciutto(cls):
        return cls(['mocarela','tomatoes','ham'])

x = Pizza.margarita()
print(x)

#dict test
#staticmethod
class Pizzastatic():
    def __init__(self, radius, ingridiens):
        self.radius = radius
        self.ingridiens = ingridiens

    def __repr__(self):
        return f'Pizza {self.ingridiens}'
    
    def area(self):
        return self._circlearea(self.radius)
    
    @staticmethod
    def _circlearea(r):
        return r ** 2 * 3.14

pizza1 = Pizzastatic(4, ["ham","cheese"])
print(pizza1.area())
print(Pizzastatic._circlearea(3))







import smtplib

server = smtplib.SMTP_SSL('smtp.aol.com', 465)
server.login('v@aol.com', 'pass')
message = "hello this is tst"

print("done")



import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "myemail@aol.com"
receiver_email = "receiver@gmail.com"
password = "app_passgen"

message = MIMEMultipart("alternative")
message["Subject"] = "subject text"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p> Text in email 
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.aol.com", 465, context=context) as server:
    server.login(sender_email, password)
    for i in range(5):
        print("send", i)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
print(message)