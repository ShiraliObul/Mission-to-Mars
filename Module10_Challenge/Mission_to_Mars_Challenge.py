#!/usr/bin/env python
# coding: utf-8

# # 10.3.3 Scrape Mars data: The news

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem


# In[6]:


news_title = slide_elem.find('div', class_='content_title').get_text()


# In[7]:


news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# # 10.3.4 Scrape Mars Data: Featured Image

# ### Featured images

# In[9]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[10]:


# This is a lot of clicking to get to the image we want. Let's start getting our code ready to automate all of the clicks.


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# # 10.3.5 Scrape Mars Data: Mars Facts

# In[15]:


url = 'https://galaxyfacts-mars.com'
browser.visit(url)


# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()


# # 10.3.6 Export to Python

# In[19]:


# Jupyter Notebook is the perfect tool for building a scraping scrip tbut fully automate we need .app


# In[20]:


# saved these codes into .py file in VS code


# # 10.4.1 Store the Data

# In[21]:


# look at the VS code, scraping py


# # Challenge code starts from here 

# In[22]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[23]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[24]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[25]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[26]:


slide_elem.find('div', class_='content_title')


# In[27]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[28]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# In[29]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[30]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[31]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[32]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[33]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[34]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[35]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[36]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[37]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[38]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for hemisphere in range(4):
    
    # Browse through each article
    full_image_elem = browser.find_by_tag('h3')
    full_image_elem[hemisphere].click()
    
    # Parse the HTML
    html = browser.html
    hemi_soup = soup(html,'html.parser')
    
    # Scraping
    title = hemi_soup.find('h2', class_='title').text
    img_url = hemi_soup.find('li').a.get('href')
    
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()


# In[39]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[40]:


# 5. Quit the browser
browser.quit()


# In[ ]:




