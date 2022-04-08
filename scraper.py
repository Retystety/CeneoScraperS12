import requests
from bs4 import BeautifulSoup as bf
response = requests.get("https://www.ceneo.pl/44978864#tab=reviews_scroll")
print(response.status_code)

page = bf(response.text, "html.praser")
opinions = page.select("div.js_product-review")
opinion = opinions.pop(0)
opinion_id = opinion["data-entry-id"]
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recomendation = opinion.select_one("span.user-post__author-recomendation > em.recommended").get_text.strip()
stars = opinion.select_one("span.user-post__score-count")
conteny opinion.select_one("div.user-post__text").get_text.strip()
published = opinion.select_one("span.user-post__published > time:nth-child(1)").["datetime"]


print(type(opinions))
print(len(opinions))
