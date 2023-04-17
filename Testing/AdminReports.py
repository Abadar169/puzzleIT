from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# specify the path to the Chrome driver executable
driver_path = '/path/to/chromedriver'

# create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=driver_path)

# navigate to the web page
driver.get('https://example.com/admin/reports')

# wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

# fill in the input fields
exam_name_input = driver.find_element_by_xpath('//input[@placeholder="Exam"]')
exam_name_input.send_keys('Exam 1')
user_name_input = driver.find_element_by_xpath('//input[@placeholder="User"]')
user_name_input.send_keys('John Doe')

# click the Search button
search_button = driver.find_element_by_xpath('//button[contains(text(), "Search")]')
search_button.click()

# wait for the table to load
time.sleep(2)

# extract data from the table
table = driver.find_element_by_tag_name('table')
rows = table.find_elements_by_tag_name('tr')
for row in rows[1:]:  # skip the header row
    cells = row.find_elements_by_tag_name('td')
    puzzle_name = cells[0].text
    user_name = cells[1].text
    date = cells[2].text
    total_clues = cells[3].text
    required_clues = cells[4].text
    clues_found = cells[5].text
    verdict = cells[6].text
    print(puzzle_name, user_name, date, total_clues, required_clues, clues_found, verdict)

# close the browser
driver.quit()
