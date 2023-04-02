from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_login:
    
    url = "https://www.zenclass.in/login"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
        
    # method to get title and current_url
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'Zen Class'
        print("SUCCESS : Web Title Captured Successfully")
        print(self.driver.current_url)
    
    #  method to login the page
    def test_login(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        
        # Retrieve the cookies before the login
        cookies_before = self.driver.get_cookies()
        
        self.driver.find_element(by=By.NAME, value=data.Login_Selectors.input_box_name).send_keys(data.Login_Data.email)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Login_Selectors.input_box_password).send_keys(data.Login_Data.password)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Login_Selectors.login_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'Zen Class'
        print("SUCCESS : LOGGED IN WITH EMAIL {email} and PASSWORD {password}".format(email=data.Login_Data.email, password=data.Login_Data.password))
        
        # Retrieve the cookies after the login
        cookies_after = self.driver.get_cookies()
                
        print('Cookies before login:', cookies_before[0]['name'])
        print('Cookies after login:', cookies_after[0]['name'])    
          
        # method to logout the webpage
        logout1=self.driver.find_element(by=By.CLASS_NAME, value="profileIcon").click()
        logout=self.driver.find_element(by=By.XPATH, value='//*[@id="root"]/nav/div/div/div/div/button[2]').click()
        print("logout sucessfully")




