from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Your Facebook login credentials
FB_EMAIL = "YOUR FACEBOOK LOGIN EMAIL"
FB_PASSWORD = "YOUR FACEBOOK PASSWORD"

# Path to ChromeDriver executable
chrome_driver_path = "C:\chromedriver.exe"  # Assuming the ChromeDriver executable is named chromedriver.exe

# Create and configure the Chrome webdriver with the specified path to ChromeDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open Tinder website
driver.get("http://www.tinder.com")

# Wait for 2 seconds before interacting with the page
sleep(2)

# Click on the login button
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

# Wait for 2 seconds before interacting with the page
sleep(2)

# Click on the Facebook login button
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

# Wait for 2 seconds before interacting with the page
sleep(2)

# Switch to the Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Find the email and password fields and enter Facebook credentials
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to the main Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# Wait for 5 seconds before interacting with the page
sleep(5)

# Allow location and notifications (assuming pop-ups appear)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    # Add a 1 second delay between likes.
    sleep(1)

    try:
        # Click on the "Like" button
        like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            # Click on the "Matched" popup
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

# Close the browser window
driver.quit()
