import requests
import json 
from bs4 import BeautifulSoup as bf
response = requests.get("https://www.ceneo.pl/44978864#tab=reviews_scroll")
print(response.status_code)

page = bf(response.text, "html.praser")
opinions = page.select("div.js_product-review")
all = []
while true:
    #opinion = opinions.pop(0)
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recomendation = opinion.select_one("span.user-post__author-recomendation > em.recommended").get_text.strip()
        except AttributeError:
            recomendation = None
        stars = opinion.select_one("span.user-post__score-count")
        conteny opinion.select_one("div.user-post__text").get_text.strip()
        published = opinion.select_one("span.user-post__published > time:nth-child(1)").["datetime"]
        pros = opinion.[item.get_text().strip() for item in pros]
        cons = opinion.[item.get_text().strip() for item in cons]
        single_option =
        {
            #tu będzie słownik
        }
        all.append(single_opinion)
    try:
        url = ""+page.select
    except TypError:
        

with open("opinions/44978864.json") as jfc:
    json.dump(all, jfc, indent=4, ensure_ascii=False)

print(type(opinions))
print(len(opinions))


    
print(json.dumps(single_opinion, indent=4, ensure_ascii=false))    

