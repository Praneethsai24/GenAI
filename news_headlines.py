import requests

url = "https://newsapi.org/v2/top-headlines?country=us&apikey=" #write my api key later
response = requests.get(url).json()

headlines = [article['title'] for article in response['article'][:5]]