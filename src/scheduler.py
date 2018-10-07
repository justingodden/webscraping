import schedule
import time
import webscraper
import pricechecker

# Scheduled task to run a web scrape daily, at 1pm
schedule.every().day.at("13:00").do(webscraper.main)

# Scheduled task to check product prices daily, at 1pm
schedule.every().day.at("13:01").do(pricechecker.checkPrice)


while True:
    schedule.run_pending()
    time.sleep(60)  # wait one minute
