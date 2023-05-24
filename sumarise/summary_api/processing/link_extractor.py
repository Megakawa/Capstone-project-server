import requests
from bs4 import BeautifulSoup

def link_extractor(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    main_content = ""

    for tag in soup.find_all(['p', 'h1']):
        main_content += tag.get_text() + '. '

    return main_content
