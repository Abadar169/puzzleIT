from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver (replace with your preferred browser)
driver = webdriver.Chrome()

# Navigate to the register page
driver.get("http://yourwebsite.com/register")

# Find the form inputs and submit button
name_input = driver.find_element(By.NAME, "name")
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# Fill in the form inputs
name_input.send_keys("John Doe")
email_input.send_keys("johndoe@example.com")
password_input.send_keys("password123")

# Submit the form
submit_button.click()

# Wait for the success message to appear
success_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'success')]"))
)

# Assert that the success message is correct
assert success_message.text == "Registration successful!"

# Close the browser
driver.quit()
