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

Additional checks you could add to the current test:
1. Check if the trust mark (Gütesiegel) is displayed and visible.
2. Verify that the latest reviews are present and visible on the page.
3. Validate that the number of reviews displayed matches the actual number of reviews.
4. Check if the overall rating is displayed in a visually prominent manner.

Next tests to consider implementing:
1. Test the functionality of sorting reviews by different criteria (e.g., date, helpfulness).
2. Test the behavior of pagination if there are multiple pages of reviews.
3. Test the functionality of clicking on a review to view its details.
4. Test the responsiveness of the page on different screen sizes (e.g., mobile, tablet).

Non-functional properties of the profile page:
1. Performance: You can test the page load time and response time under different network conditions to ensure it meets performance requirements.
2. Accessibility: Conduct accessibility testing to verify if the page is accessible to users with disabilities, adhering to WCAG guidelines.
3. Security: Perform security testing to identify vulnerabilities and ensure that user data is protected.
4. Cross-browser compatibility: Test the page on different web browsers (e.g., Chrome, Firefox, Safari) to ensure consistent behavior and appearance.
5. Usability: Conduct user testing and gather feedback to evaluate the page's usability and identify areas for improvement.
6. Localization: Test the page with different languages and verify that all elements are correctly translated and displayed.
7. Scalability: Perform load testing to determine how the page handles a large number of concurrent users and ensure it can scale effectively.
8. Error handling: Test error scenarios, such as entering invalid inputs or encountering server errors, and verify that the page handles them gracefully.
9. Browser compatibility: Test the page on different browsers and versions to ensure it renders correctly and functions properly across a wide range of environments.
10. Cross-device testing: Test the page on different devices (e.g., desktop, laptop, tablet, mobile) to ensure it is responsive and displays correctly on all screen sizes.
11. Localization and internationalization: Test the page with different languages, regions, and locales to ensure proper translation and formatting of content.
12. Performance and load testing: Test the page's performance and load handling capabilities by simulating high traffic and measuring response times and resource usage.
13. Compatibility testing: Test the page with different operating systems, browsers, and versions to ensure compatibility and consistent behavior.
14. Security testing: Conduct security assessments to identify vulnerabilities such as cross-site scripting (XSS), SQL injection, and data leakage.
15. Accessibility testing: Evaluate the page's accessibility for users with disabilities by adhering to accessibility standards (e.g., WCAG 2.1) and conducting usability tests with assistive technologies.
16. Usability testing: Gather user feedback through usability tests and surveys to evaluate the page's user-friendliness, navigation, and overall user experience.

Note: Make sure to avoid creating a heavy load on the Trusted Shops page while executing the test.
