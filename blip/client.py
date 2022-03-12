from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4


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

    @property
    def last_message(self):
        pass
