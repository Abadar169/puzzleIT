from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Open the browser and navigate to the login page
driver = webdriver.Chrome()
driver.get("http://localhost:3000/login")

# Find the email and password input fields, and fill them with valid credentials
email_input = driver.find_element_by_name("email")
password_input = driver.find_element_by_name("password")
email_input.send_keys("user@example.com")
password_input.send_keys("password")

# Click the login button
login_button = driver.find_element_by_css_selector(".button")
login_button.click()

# Wait for the page to load and check if the user is redirected to the home page
wait = WebDriverWait(driver, 10)
home_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome to PuzzleIt']")))
assert home_page.is_displayed()

# Log out by clearing the local storage
driver.execute_script("window.localStorage.clear()")

# Check if the user is redirected to the login page after logging out
login_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login")))
assert login_page.is_displayed()

# Close the browser
driver.quit()
