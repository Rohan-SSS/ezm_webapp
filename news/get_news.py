# Currently using https://forexnewsapi.com/ free data, possible approac is to automate scrapping daata from there 
# or buy the api, or make a custom scraper using forex factory and bs4

import json

file_path = 'news/news_eurusd.json'

def get_news():
    news_data = []
    with open(file_path, 'r') as news:
        json_content = news.read()
        json_data = json.loads(json_content)

        for i in range(10):
            news_data.append(json_data["data"][i])

    return news_data

