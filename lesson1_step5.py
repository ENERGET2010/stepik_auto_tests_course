import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')
    
    time.sleep(0.5)
    
#     treasure = browser.find_element(By.ID, 'treasure')
#     x_element = treasure.get_attribute('valuex')
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()
    
    
    
    
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()
    
    
finally:
    time.sleep(30)
    browser.quit()
    