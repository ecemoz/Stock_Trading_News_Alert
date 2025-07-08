# Tesla Stock Alert & News Mailer

This Python script tracks Tesla's (TSLA) stock price using the Alpha Vantage API. If the daily price change exceeds 5%, it fetches the latest news headlines related to Tesla via the NewsAPI and sends them to your email using Gmail's SMTP server.

---

## 🔧 Features

* Fetches daily TSLA stock prices
* Compares the last two closing prices
* If change > 5%, fetches the latest news headlines (max 3)
* Sends formatted news via email

---

## 📚 Requirements

* Python 3.x
* Required libraries:

  ```bash
  pip install requests
  ```

---

## 📦 Setup & Configuration

### 1. **Alpha Vantage API Key**

* Register: [https://www.alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key)
* Replace `STOCK_API_KEY` in the script.

### 2. **NewsAPI Key**

* Register: [https://newsapi.org/register](https://newsapi.org/register)
* Replace `NEWS_API_KEY` in the script.

### 3. **Gmail SMTP Setup**

* Go to: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
* Generate a 16-character app password (requires 2FA enabled)
* Replace `app_password` in the script.

### 4. **Sender & Receiver Emails**

* `my_email`: your Gmail address
* `to_email`: where the alert email will be sent

---

## 🔄 How It Works

```python
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
```

* Gets time series stock data from Alpha Vantage.

```python
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
```

* Extracts closing prices for the last 2 days.

```python
diff_percent = (difference / float(yesterday_closing_price)) * 100
```

* Calculates price change in percentage.

```python
if diff_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
```

* If change exceeds 5%, fetches top 3 news headlines.

```python
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.login(user=my_email, password=app_password)
```

* Sends the formatted news email via Gmail SMTP.

---

## ⏳ Automate on PythonAnywhere (Optional)

1. Upload this script to your PythonAnywhere Files section.
2. Test in **Bash Console**:

   ```bash
   python3 main.py
   ```
3. Set up a **Scheduled Task** (e.g., every day at 09:00):

   ```bash
   python3 /home/yourusername/main.py
   ```

---

## 🚨 Troubleshooting

* **KeyError: 'Time Series (Daily)'**

  * Cause: API rate limit or invalid API key
  * Fix: Wait 1 min or print `response.json()` to inspect

* **SMTPAuthenticationError**

  * Cause: Incorrect Gmail or app password
  * Fix: Use Gmail app password, not your main password

---

## 🌟 Future Ideas

* HTML formatted email
* Support for multiple stocks
* Telegram bot alerts

---

## 📄 License

MIT License

---

Happy coding! 🚀
