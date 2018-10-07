import pandas as pd
import emailer


def checkPrice():
    # Checks whether at least one of the products is less than £1000
    answer = 'false'
    df = pd.read_csv("products.csv")
    for i in df[' price']:
        if float(i) < 1000:
            answer = "true"

    # If item is on sale, email user
    if answer == "true":
        emailer.main()
