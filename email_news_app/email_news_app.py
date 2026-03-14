import requests
from send_email import send_email

topic = "tesla"

#To get the API Key from this website:  https://newsapi.org/
api_key = "xxxxxx"

#copy URL value from the Get:
url = "https://newsapi.org/v2/everything?"\
       f"q={topic}&"\
       "sortBy=publishedAt&"\
       "apiKey=xxxxxxx&"\
        "language=en"

#make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#access the article title and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news "+ "\n"+ body + article["title"] + "\n" + str(article["description"])+ "\n"+article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)


