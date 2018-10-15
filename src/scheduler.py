import schedule
import time
import webscraper
import pricechecker
import emailer


# Initialise the scrape object
url = 'https://www.overclockers.co.uk/pc-components/graphics-cards/nvidia/geforce-rtx-2080-ti'
scrape = webscraper.WebScrape(url)


# Function to run all scrape methods in order
def full_scrape():
    scrape.findIDs()
    scrape.findBrands()
    scrape.findNames()
    scrape.findPrices()
    scrape.createSpreadsheet()


# Scheduled task to run a web scrape daily, at 1pm
schedule.every().day.at("13:00").do(full_scrape)

# Scheduled task to check product prices daily, at 1pm
schedule.every().day.at("13:01").do(pricechecker.checkPrice)


while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
