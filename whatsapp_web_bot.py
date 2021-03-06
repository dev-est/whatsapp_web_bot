import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class whatsapp:
    
    def whatsapp_login(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("user-data-dir=YOUR-DIRECTORY-HERE")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        base_url = "https://web.whatsapp.com/"
        self.driver.get(base_url)
        
    def whatsapp_message(self,name,message):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, f"//span[@title='{name}']"))).click()
        self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
        self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        
    def whatsapp_close(self):
        self.driver.close()


if __name__ == "__main__":
    #initialise login
    whatsapp = whatsapp()
    whatsapp.whatsapp_login()
    receive = input("Who would you like to message? ")
    message = input("Please enter your message ")
    whatsapp.whatsapp_message(receive,message)
    time.sleep(3)
    whatsapp.whatsapp_close()