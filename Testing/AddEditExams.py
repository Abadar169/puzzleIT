import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AddEditExamsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_add_exam(self):
        driver = self.driver
        driver.get("http://localhost:3000/admin/exams")

        # Click on "Add Puzzle" button
        add_puzzle_btn = driver.find_element_by_xpath("//button[contains(text(), 'Add Puzzle')]")
        add_puzzle_btn.click()

        # Fill out form
        name_input = driver.find_element_by_name("name")
        name_input.send_keys("Test Puzzle")
        duration_input = driver.find_element_by_name("duration")
        duration_input.send_keys("60")
        category_select = driver.find_element_by_name("category")
        category_select.send_keys("Critical Thinking")
        total_marks_input = driver.find_element_by_name("totalMarks")
        total_marks_input.send_keys("10")
        passing_marks_input = driver.find_element_by_name("passingMarks")
        passing_marks_input.send_keys("7")
        save_btn = driver.find_element_by_xpath("//button[contains(text(), 'Save')]")
        save_btn.click()

        # Verify success message is displayed
        success_msg = driver.find_element_by_xpath("//div[contains(@class, 'ant-message-success')]")
        self.assertTrue(success_msg.is_displayed())

    def test_edit_exam(self):
        driver = self.driver
        driver.get("http://localhost:3000/admin/exams")

        # Click on first exam in table
