import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK_NAME = "TSLA"
COMPANY_NAME= "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY= "WEE1V7MHCLPIOHH3"
NEWS_API_KEY = "898195e743aa42c4b22044ab041473c2"


stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : STOCK_API_KEY,
}


response = requests.get(STOCK_ENDPOINT, params = stock_params)
data = response.json() ["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

if diff_percent > 5:
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json() ["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles = [
        f"Headline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

my_email = "ecemnurozen03@gmail.com"
to_email = "emreuslu256@gmail.com"
app_password = "uprq nkeq yutu ztoe"

message = MIMEMultipart("alternative")
message["Subject"] = "🚨 Tesla hissesi %5'ten fazla değişti!"
message["From"] = my_email
message["To"] = to_email

news_content = "\n\n".join(formatted_articles)
text_part = MIMEText(news_content, "plain")
message.attach(text_part)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_email,
        msg=message.as_string()
    )

print(" Mail başarıyla gönderildi.")
