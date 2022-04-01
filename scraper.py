import requests
response = requests.get("https://www.ceneo.pl/44978864#tab=reviews_scroll")
print(response.status_code)