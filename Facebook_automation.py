from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the Chrome browser
options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)



# Navigate to Facebook
driver.get("https://www.facebook.com")

# Find the username and password input fields and enter your credentials
username_input = driver.find_element(By.ID,"email")
password_input = driver.find_element(By.ID,"pass")

username = "YourUsername"  # Replace with your Facebook username
password = "YourPassword"  # Replace with your Facebook password

username_input.send_keys(username)
password_input.send_keys(password)

# Submit the form (login)
password_input.send_keys(Keys.RETURN)


WebDriverWait(driver, 10)  # Wait for up to 10 seconds

