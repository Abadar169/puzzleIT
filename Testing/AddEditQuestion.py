# This test case assumes that the modal appears when the "Add Question" button is clicked, and that the success message appears when the question is successfully added. If the behavior of the component changes, the test case may need to be updated accordingly.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Navigate to the page with the AddEditQuestion component
driver.get("http://yourwebsite.com")

# Find and click the button that triggers the modal
add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Question')]")
add_button.click()

# Wait for the modal to appear
wait = WebDriverWait(driver, 10)
modal = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='ant-modal-content']")))

# Fill out the form
question_input = modal.find_element(By.NAME, "name")
question_input.send_keys("Sample question")

correct_option_input = modal.find_element(By.NAME, "corrrectOption")
correct_option_input.send_keys("A")

option_a_input = modal.find_element(By.NAME, "A")
option_a_input.send_keys("Option A")

option_b_input = modal.find_element(By.NAME, "B")
option_b_input.send_keys("Option B")

option_c_input = modal.find_element(By.NAME, "C")
option_c_input.send_keys("Option C")

option_d_input = modal.find_element(By.NAME, "D")
option_d_input.send_keys("Option D")

# Submit the form
save_button = modal.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
save_button.click()

# Wait for the success message to appear
success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Question added successfully')]")))

# Close the modal
close_button = modal.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
close_button.click()

# Verify that the question was added
# (you could do this by checking if the new question appears in the list of questions)
