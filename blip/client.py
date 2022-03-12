from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class BlipTestClient:
    def __init__(self, name, app_key):
        self.name = name
        self.__app_key = app_key
        self.__blip_url = f'https://chat.blip.ai/?appKey={self.__app_key}'

    def start_chat(self, options=None):
        self.__driver = webdriver.Firefox(options=options)
        self.__driver.get(self.__blip_url)

    def send_message(self, message):
        message_box = self.__driver.find_element_by_id('msg-textarea')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)

    def close_chat(self):
        self.__driver.close()

    def __transform_card_to_message(self, html):
        message = html.find('div', {'class': ['bubble', 'left']})

        text = message.find('div').text.replace('\n', '<br>')
        hour = html.find('div', {'class': 'flex'}).find('div').text

        return {"text": text, "hour": hour}

    def __extract_messages_from_html(self, html):
        soup = BeautifulSoup(html, features='lxml')
        messages_cards = soup.find_all(
            'div', {'class': 'blip-container plain-text'})

        messages = []

        for message_card in messages_cards:
            message = self.__transform_card_to_message(message_card)
            messages.append(message)

        return messages

    def last_messages(self, size):
        html = self.__driver.page_source
        messages = self.__extract_messages_from_html(html)

        return messages[-size:]

    @property
    def last_message(self):
        message = self.last_messages(size=1)

        if len(message) == 0:
            return None

        return message[0]

    @property
    def empty(self):
        return len(self.last_message) == 0
