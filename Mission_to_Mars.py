# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

## Article scraping example

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# searching for elements with "div" tag and "list_text" attribute
# wait one second for page to load

html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')
# div is our parent element to be searched

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `div` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

## Image scraping example

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1] # Index specifies that we want to click the second "button"
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

## Table scraping example

df = pd.read_html('https://galaxyfacts-mars.com')[0] # Search for tables in the HTML and only return the first, create a DF
df.columns=['description', 'Mars', 'Earth'] # Assign column names to the df
df.set_index('description', inplace=True) # Turn the description column into the DF index
df

# Convert DF back to HTML to keep it dynamic, for use on a webpage
df.to_html()

## Turn off the web browser, end the session
browser.quit()