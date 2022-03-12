from selenium import webdriver
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
        self.__driver.find_element_by_id('msg-textarea').send_keys(message)
        self.__driver.find_element_by_id('blip-send-message').click()

    def close_chat(self):
        self.__driver.close()
