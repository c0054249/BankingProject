import requests
from bs4 import BeautifulSoup


def fetch_top_stories(url, count=4):
    response = requests.get(url)

    if response.status_code != 200:
        raise ValueError(f"Failed to fetch the URL {url}. Status code: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")
    parent_element = soup.find("div", class_="o-teaser-collection o-teaser-collection--stream")
    stories = parent_element.find_all("div", class_="o-teaser", limit=count)

    top_stories = []

    for story in stories:
        headline_element = story.find("div", class_="o-teaser__heading")
        headline = headline_element.text.strip()

        # Extract hyperlink
        link_element = headline_element.find("a")
        hyperlink = 'https://www.ft.com' + link_element["href"]

        image_element = story.find("img", class_="o-teaser__image o-lazy-load")
        if image_element is not None:
            picture = image_element.get("src") or image_element.get("data-src")
        else:
            picture = 'static\stock-bank-image.jpg'

        top_stories.append({"headline": headline, "picture": picture, "hyperlink": hyperlink})

    return top_stories


def init_web_scraping():
    url = "https://www.ft.com/uk-banks"
    top_stories = fetch_top_stories(url)
    return top_stories
