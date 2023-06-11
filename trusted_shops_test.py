# importing necessary modules:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver instance and open the desired URL:

driver = webdriver.Chrome()  # Assumes Chrome WebDriver is in PATH
driver.maximize_window()  # Ensures desktop view (> 1000px width)
url = "https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html"
driver.get(url)

# Implement the test steps:

# Check if the page title exists:

page_title = driver.title
assert page_title != ""

# Check if the grade is visible and above zero:

grade_element = driver.find_element(By.CLASS_NAME, "ts-rating-grade")
grade_text = grade_element.text
assert float(grade_text) > 0.0

# Check if the "Wie berechnet sich die Note?" link opens the window with relevant information:

wie_berechnet_link = driver.find_element(By.LINK_TEXT, "Wie berechnet sich die Note?")
wie_berechnet_link.click()

# Switch to the newly opened window
driver.switch_to.window(driver.window_handles[-1])

# Perform assertions on the relevant information
# ...

# Close the new window and switch back to the main window
driver.close()
driver.switch_to.window(driver.window_handles[0])

# Click on "2 Stars" to filter all "two stars" reviews and verify the filter is applied correctly:

stars_filter = driver.find_element(By.XPATH, "//span[text()='2 Sterne']")
stars_filter.click()

# Verify that every review in the entire list has only two stars
# ...

# Clear the filter to restore the original list
stars_filter.click()


# Create the sum of all star percentage values and ensure it's equal or below 100:

star_percentage_elements = driver.find_elements(By.CLASS_NAME, "ts-rating-stars")
star_percentage_sum = 0
for element in star_percentage_elements:
    star_percentage_sum += int(element.text.replace("%", ""))
assert star_percentage_sum <= 100


# Close the WebDriver and quit the browser:
driver.quit()
