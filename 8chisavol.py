import requests
from bs4 import BeautifulSoup


def scrape_daily_news(url):
    try:
        # Fetching the HTML content of the page
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Finding elements with class "news" (assuming it contains the daily news)
            news_elements = soup.find_all(class_="news")

            # Extracting and printing daily news headlines
            for news in news_elements:
                print(news.get_text())
        else:
            print("Failed to fetch the webpage. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)


url = "https://tribuna.uz/"

scrape_daily_news(url)
