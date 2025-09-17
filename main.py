import requests
from datetime import date
from time import sleep

dt = date.today()
date = f"{dt.year}-{dt.month}-{int(dt.day)-2}"

cancel = ["no", "No", "NO", "nope", "Nope", "NOPE", "n", "N"]

while True:
    query = input("What type of news are you interested in? ")
    api = "83b03f55a20448a78e948728a7de25e1"

    url = f"https://newsapi.org/v2/everything?q={query}&from={date}&to={date}&sortBy=relevancy&pageSize=5&apiKey={api}"

    print(url)
    r = requests.get(url)

    data= r.json()
    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index + 1, article["title"])
        print(article["description"])
        print(article["url"])
        print("\n****************************************\n")

    if input("Do you want to search for another topic? ") in cancel:
        break
