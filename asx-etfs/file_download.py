from selenium import webdriver

# Set up the Chrome WebDriver
driver = webdriver.Firefox()

# Open the webpage
driver.get('https://www.asx.com.au/markets/trade-our-cash-market/asx-investment-products-directory/etps')

# Wait for necessary elements to load or interact with the page
driver.implicitly_wait(10)  # waits for 10 seconds

# Get page source
html_source = driver.page_source

with open('page_source.html', 'w', encoding='utf-8') as file:
    file.write(html_source)
    
# You can now use html_source with BeautifulSoup or other tools
# Remember to close the driver
driver.quit()
