import requests
import string
from bs4 import BeautifulSoup as bs
from lxml import etree
from tqdm import tqdm


URL = "https://www.siruvarmalar.com/kids-stories-list"

page = requests.get(
    URL,
    headers={
        "User-rAgent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
    },
)
soup = bs(page.content, "html.parser")

dom = etree.HTML(str(soup))
links = dom.xpath('//*[@id="lcp_instance_0"]/li/a/@href')[1:]

print(f"SCRAPING {len(links)} STORIES...")


for ix, link in enumerate(tqdm(links)):
    text = ""
    page = requests.get(
        link,
        headers={
            "User-rAgent": "Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36"
        },
    )
    soup = bs(page.content, "html.parser")

    p_tags = soup.find_all("p")

    for tag in p_tags:
        txt = tag.text.strip()
        if txt == "":
            pass
        else:
            if txt[0] in string.ascii_letters:
                pass
            else:
                text += txt + "\n"
    # print(text)

    with open(f"../data/txt_files/tamil/ta_{ix}.txt", "w") as f:
        f.write(text)

print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t******** COMPLETED *********")
