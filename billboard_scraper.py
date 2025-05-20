import requests
from bs4 import BeautifulSoup
from typing import List

class BillboardScraper:
    def __init__(self, date):
        self.date = date
        self.url = f"https://www.billboard.com/charts/hot-100/{self.date}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
        }
        self.billboard_song_list = []

    def scrap_billboard(self) -> List[str]:
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.text, "lxml")
        title_tags = soup.find_all(
            "h3",
            id="title-of-a-story",
            class_="a-no-trucate"
        )

        for title in title_tags:
            new_title = title.text.replace("\n", "").replace("\t", "")
            self.billboard_song_list.append(new_title)
        return self.billboard_song_list



# test = BillboardScraper("2002-08-15")
# print("BILLBOARD LIST: ", test.scrap_billboard())