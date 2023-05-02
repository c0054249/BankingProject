import requests
from bs4 import BeautifulSoup


# exception class
class FetchError(Exception):
    pass


def fetch_top_stories(url, count=4):
    response = requests.get(url)

    # if the html does not return a 200 code raise error
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch the URL {url}. Status code: {response.status_code}")

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        parent_element = soup.find("div", class_="o-teaser-collection o-teaser-collection--stream")
        stories = parent_element.find_all("div", class_="o-teaser", limit=count)
    except AttributeError as e:
        raise FetchError(f"Error while parsing the HTML content. Error: {str(e)}")

    top_stories = []

    for story in stories:
        # extract headline
        headline_element = story.find("div", class_="o-teaser__heading")
        if headline_element:
            headline = headline_element.text.strip()

            # extract hyperlink
            link_element = headline_element.find("a")
            if link_element:
                hyperlink = 'https://www.ft.com' + link_element["href"]
            else:
                hyperlink = None
        else:
            headline = None

        # extract image
        image_element = story.find("img", class_="o-teaser__image o-lazy-load")
        if image_element is not None:
            picture = image_element.get("src") or image_element.get("data-src")
        else:
            picture = 'static\stock-bank-image.jpg'

        top_stories.append({"headline": headline, "picture": picture, "hyperlink": hyperlink})

    return top_stories


def init_web_scraping():
    url = "https://www.ft.com/uk-banks"
    try:
        top_stories = fetch_top_stories(url)
        return top_stories
    except FetchError as e:
        print(str(e))
        return []
