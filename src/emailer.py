import smtplib


class Emailer:
    def __init__(self, email="", password="", subject="", message=""):
        self.email = email
        self.password = password
        self.subject = subject
        self.message = message

    def serverConnect(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password)

    def sendMail(self, subject, message):
        msg = "Subject: {}\n\n{}".format(self.subject, self.message)
        self.server.sendmail(self.email, self.email, msg)
        self.server.quit()
