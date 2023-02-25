import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
import requests
from lxml import etree
import os

df = pd.read_csv("../data/metadata/subset.csv")
print(df.head())

BASE_LINK = "https://www.gutenberg.org/"
SAVE_DIR = "../data/txt_files/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}

print(f"\nDOWNLOADING TXT FILES OF {len(df)} BOOKS.\n")

for ix in tqdm(range(len(df))):
    data = df.iloc[ix]
    book_id = data["Link"].split("/")[-1]
    url = BASE_LINK + "files/" + book_id
    page = requests.get(url=url, headers=HEADERS)
    soup = bs(page.content, "html.parser")
    links = etree.HTML(str(soup))
    links = links.xpath("*//a/@href")

    for link in links:
        if link == f"{book_id}.txt":
            book = requests.get(url=url + "/" + link, headers=HEADERS)
            s = bs(book.content, "html.parser")
            with open(os.path.join(SAVE_DIR, link), "w") as f:
                f.write(s.prettify())
        else:
            pass


print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t******** COMPLETED *********")
