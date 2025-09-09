from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()

driver.get("https://www.saucedemo.com/")



driver.find_element(By.ID, "user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
select = Select(sort_dropdown)

time.sleep(1)

select.select_by_value("hilo")

time.sleep(1)

first_item = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
add_button = first_item.find_element(By.TAG_NAME, "button")
add_button.click()

time.sleep(1)

cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()

time.sleep(1)

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# time.sleep(1)

# driver.find_element(By.ID, "first-name").send_keys("Dmitriy")
# driver.find_element(By.ID, "last-name").send_keys("Shergin")
# driver.find_element(By.ID, "postal-code").send_keys("664074")

# time.sleep(1)

# continue_button = driver.find_element(By.ID, "continue")
# continue_button.click()

# time.sleep(1)

# finish_button = driver.find_element(By.ID, "finish")
# finish_button.click()

# time.sleep(1)

# back_to_products_button = driver.find_element(By.ID, "back-to-products")
# back_to_products_button.click()

time.sleep(10)

driver.quit()