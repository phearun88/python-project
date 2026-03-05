import requests
from send_email import send_email

#To get the API Key from this website:  https://newsapi.org/
api_key = "xxxxxx"

#copy URL value from the Get:
url = "https://newsapi.org/v2/everything?q=tesla&from=2026-02-05&sortBy=publishedAt&apiKey=xxxxxxx"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#access the article title and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)


