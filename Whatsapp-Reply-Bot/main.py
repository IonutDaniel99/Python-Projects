from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--user-data-dir=./User_Data')
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)


class WhatsappBot():
    def __init__(self):
        driver.get("https://web.whatsapp.com/")
        self.Check_For_Page()

    def Check_For_Page(self):
        time.sleep(20)
        if driver.find_elements_by_class_name("landing-wrapper"):
            print("Landing Page")
            time.sleep(10)
            self.Check_For_Page()
        elif driver.find_elements_by_class_name("app._1Jzz1.two"):
            self.OnFirstStart()

    def OnFirstStart(self):
        whatsapp_user_info = []
        for person in driver.find_elements_by_class_name('X7YrQ'):
            title = person.find_element_by_xpath(
                'div/div/div[2]/div[1]/div[1]/span').text
            notify = person.find_element_by_xpath(
                'div/div/div[2]/div[2]/div[2]/span').text
            time = person.find_element_by_xpath(
                'div/div/div[2]/div[1]/div[2]').text
            if notify != '':
                whatsapp_user_info.append((title, time, notify))
        self.save_to_file(whatsapp_user_info)
        self.bot_start(whatsapp_user_info)

    def save_to_file(self, whatsapp_user_info):
        status = ["Not Important", "Normal", "Urgent", "Critical"]
        type_of_status = ''
        with open("Data/Recipient_Details.txt", "a", encoding='utf-8') as f:
            _equal = "=" * 34
            f.write("\n" + _equal +
                    datetime.now().strftime("%H:%M:%S / %d-%m-%Y") + _equal + "\n")
            for lines in whatsapp_user_info:
                if int(lines[2]) < 5:
                    type_of_status = status[0]
                elif int(lines[2]) > 5:
                    type_of_status = status[1]
                elif int(lines[2]) > 10:
                    type_of_status = status[2]
                elif int(lines[2]) > 25:
                    type_of_status = status[3]
                f.write("Name = %s / Last Message At : %s / No. Messages = %s / Status = %s \n" %
                        (lines[0], lines[1], lines[2], type_of_status))
            f.close()

    def bot_start(self, whatsapp_user_info):
        send_button = driver.find_element_by_xpath(
            "//button[@class='_3M-N-']")
        text_area = driver.find_element_by_xpath(
            "//div[@class='_3u328 copyable-text selectable-text']")

        for lines in whatsapp_user_info:
            if lines[0] == "x":  # Instead of X put the name of recipients or group
                driver.find_element_by_xpath(
                    "//span[contains(text(), '" + lines[0] + "')]").click()
                text_area.send_keys("text")
                send_button.click()

            if lines[0] == "y":  # Instead of Y put the name of recipients or group
                driver.find_element_by_xpath(
                    "//span[contains(text(), '" + lines[0] + "')]").click()
                text_area.send_keys("text")
                send_button.click()

            if lines[0] == "z":  # Instead of Z put the name of recipients or group
                driver.find_element_by_xpath(
                    "//span[contains(text(), '" + lines[0] + "')]").click()
                text_area.send_keys("text")
                send_button.click()


bot = WhatsappBot()
bot.__init__()
