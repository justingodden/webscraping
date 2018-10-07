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


# Input user's email address, email pass word, and the subject and message to send
email = ""
password = ""
subject = "GTX 2080ti on sale"
message = "Good news! The NVidia RTX 2080ti is now below £1000. Maybe time for an upgrade?"

EM = Emailer(email, password, subject, message)


def main():
    EM.serverConnect()
    EM.sendMail(subject, message)
