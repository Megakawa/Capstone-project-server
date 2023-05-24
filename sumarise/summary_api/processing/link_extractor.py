import requests
from bs4 import BeautifulSoup

def link_extractor(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
        tag.extract()


    main_content = soup.get_text()

    return main_content
