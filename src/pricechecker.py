import pandas as pd
import emailer


# Initialse all email details and build emailer object
email = ""
password = ""
subject = "RTX 2080ti on sale"
message = "Good news! The NVidia RTX 2080ti is now below £1000. Maybe time for an upgrade?"

EM = emailer.Emailer(email, password, subject, message)


def full_email():
    EM.serverConnect()
    EM.sendMail(subject, message)


def checkPrice():
    # Checks whether at least one of the products is less than £1000
    answer = 'false'
    df = pd.read_csv("products.csv")
    for i in df[' price']:
        if float(i) < 1000:
            answer = "true"

    # If item is on sale, email user
    if answer == "true":
        full_email()
