import requests
from bs4 import BeautifulSoup
import pandas as pd

Product_url = []
Product_name = []
Product_price = []
Product_rating = []
Product_reviews = []
try:
    for i in range(1, 21):
        url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1685175675&sprefix=ba%2Caps%2C283&ref=sr_pg_1" + str(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")  # Use html.parser instead of lxml

        box = soup.find("div", class_="sg-col-inner")
        if box:
            name = box.find_all("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2")
            for i in name:
                n = i.text
                Product_name.append(n)

            price = box.find_all("span", class_="a-offscreen")
            for i in price:
                p = i.text
                Product_price.append(p)

            rating = box.find_all("span", class_="a-icon-alt")
            for i in rating:
                ra = i.text
                if ra != 'null':
                    Product_rating.append(ra)
                else:
                    Product_rating.append('NA')

            reviews = box.find_all("span", class_="a-size-base s-underline-text")
            for i in reviews:
                re = i.text
                if re != 'null':
                    Product_reviews.append(re)
                else:
                    Product_reviews.append('NA')
except AttributeError:
    pass
if len(Product_name) == len(Product_price) == len(Product_rating) == len(Product_reviews) == len(Product_url):
    # data storing
    df = pd.DataFrame({"ProductName": Product_name, "ProductPrice": Product_price, "ProductRating": Product_rating, "ProductReviews": Product_reviews, "Product url": Product_url})
    df.to_csv("PageData1.csv")
    print("Successful")
else:
    # Adjust array lengths by assigning placeholder values or skipping incomplete data
    max_length = max(len(Product_name), len(Product_price), len(Product_rating), len(Product_reviews), len(Product_url))
    Product_name.extend(['NA'] * (max_length - len(Product_name)))
    Product_price.extend(['NA'] * (max_length - len(Product_price)))
    Product_rating.extend(['NA'] * (max_length - len(Product_rating)))
    Product_reviews.extend(['NA'] * (max_length - len(Product_reviews)))
    Product_url.extend(['NA'] * (max_length - len(Product_url)))
