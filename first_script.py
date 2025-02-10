import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    time.sleep(3)

    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(1)

    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

    textarea.send_keys("get()")
    time.sleep(1)

    # Найдем кнопку, которая отправляет введенное решение
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
    submit_button.click()
    time.sleep(5)

finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()
