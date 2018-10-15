from bs4 import BeautifulSoup as soup
import urllib


class WebScrape:

    def __init__(self, url=''):
        self.url = url
        # Open url
        uClient = urllib.request.urlopen(self.url)
        # Download all the html
        page_html = uClient.read()
        # Close url
        uClient.close()
        # Parse html
        self.page_soup = soup(page_html, "html.parser")

    def findIDs(self):
        # Unique Product ID
        IDtag = self.page_soup.findAll("a", {"class": "producttitles"})
        self.IDs = []
        for ID in range(len(IDtag)):
            self.IDs.append(IDtag[ID]["data-id"])

    def findBrands(self):
        # Find Brand Name
        brandtag = self.page_soup.findAll("span", {"class": "ProductSubTitle"})
        self.brands = []
        for brand in range(len(brandtag)):
            self.brands.append(brandtag[brand].get_text().strip())

    def findNames(self):
        # Find Product Name
        nametag = self.page_soup.findAll("span", {"class": "ProductTitle"})
        self.names = []
        for name in range(len(nametag)):
            self.names.append(nametag[name].get_text().strip())

    def findPrices(self):
        # Find Price
        pricetag = self.page_soup.findAll("span", {"class": "price"})
        self.prices = []
        for price in range(len(pricetag)):
            self.prices.append(pricetag[price].get_text().strip())

    def createSpreadsheet(self):
        # Create Spreadsheet
        filename = "products.csv"
        f = open(filename, "w")

        # Spreadsheet Headers
        headers = "product_ID,brand,product_name,price\n"
        f.write(headers)

        # Save Data in CVS Spreadsheet
        for i in range(len(self.IDs)):
            f.write(self.IDs[i]+","+self.brands[i]+","+self.names[i] +
                    ","+self.prices[i].replace("£", "").replace(",", "")+"\n")
        f.close()
