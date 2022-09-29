from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import utils

MAX_WAIT_LOGIN = 60

class BlipClient:
    def __init__(self, receiver, headless=True):
        service = Service(executable_path="C:/chromedriver/chromedriver.exe")
        options = utils.create_options(Options(), headless)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.receiver = receiver
        self.__start__()
    
    def __open_whatsapp__(self):
        self.driver.get(f"https://web.whatsapp.com/send?phone={self.receiver}")
    
    def __clear_messages__(self):
        self.driver.find_element(By.XPATH,'//*[@id="main"]/header/div[3]/div/div[2]').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/span[4]/div/ul/div/div/li[7]').click()
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div').click()
    
    
    def __hide_conversations__(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[3]/header/div[1]/div').click()
        
    def __waiting_login__(self):
        for i in range(MAX_WAIT_LOGIN):
            try:
                self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
                return True
            except:
                time.sleep(1)
        return False
    
    def __start__(self):
        self.__open_whatsapp__()
        
        if self.__waiting_login__():
            self.__hide_conversations__()
            self.__clear_messages__()
        else:
            print('ERRO: Falha ao Autenticar')

    def send_message(self, message):
        self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(message)
        self.driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()