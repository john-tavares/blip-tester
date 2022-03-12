from requests import Session
import bs4


class BlipTestClient:
    def __init__(self, name, app_key):
        self.name = name
        self.__app_key = app_key
        self.__blip_url = f'https://chat.blip.ai/?appKey={self.__app_key}'
        self.__session = Session()

    def __search_element_in_html(self, value, element_type='id'):
        response = self.__session.get(self.__blip_url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        if element_type == 'class':
            return soup.find_all("div", {"class": value})

        elif element_type == 'id':
            return soup.find_all(id=value)

    @property
    def is_publicated(self):
        bot_name = self.__search_element_in_html(
            'blip-chat-bot-name', 'class')

        if bot_name == []:
            return False

        return True
