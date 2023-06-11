# TestTask

Trusted Shops End-to-End Test
This is an End-to-End test script written in Python using Selenium and Chrome WebDriver. The script performs various checks on a Trusted Shops customer profile page.

Prerequisites
1. Python 3.x installed (https://www.python.org/downloads/)
2. Selenium library installed (pip install selenium)
3. Chrome WebDriver compatible with your Chrome browser version (https://sites.google.com/a/chromium.org/chromedriver/downloads)


Execution


1. Clone this repository or download the trusted_shops_test.py file.

2. Install the necessary dependencies by running the following command in your terminal:
pip install selenium

3. Ensure that the Chrome WebDriver executable is accessible in your system's PATH.

4. Open a terminal and navigate to the directory containing the trusted_shops_test.py file.

5. Execute the test script by running the following command:
python trusted_shops_test.py

Test Steps:

1. Check if the page title exists.
2. Check if the grade is visible and above zero (e.g., 4.81/5.00).
3. Click on "Wie berechnet sich die Note?" link and verify the displayed information.
4. Click on "2 Stars" to filter all "two stars" reviews and ensure the filter is applied correctly.
5. Calculate the sum of all star percentage values and ensure it's equal to or below 100.

Further Development

Here are some ideas for further development:

1. Expand the test to cover additional scenarios such as validating trust mark status and specific review details.
2. Implement error handling and reporting mechanisms for better feedback in case of test failures.
3. Integrate the test into a test automation framework for improved test management and reporting.
4. Parameterize the test to allow testing different customer profile pages.
5. Implement test data generation or mocking for test repeatability and independence.
6. Consider implementing test data cleanup mechanisms to restore the original state of the customer profile page.
7. Feel free to modify and enhance the test script and the README file based on your specific requirements and preferences.

Note: Make sure to avoid creating a heavy load on the Trusted Shops page while executing the test.
