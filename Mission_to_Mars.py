
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs


# In[2]:


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


# Visit the Nasa Mars site
url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(url)


# In[4]:


# Scrape page into soup
html = browser.html
soup = bs(html, "html.parser")

    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 
    # Assign the text to variables that you can reference later.Find today's forecast
    
MarsNews = soup.find("div", class_="content_title")

MarsNewsTitle = MarsNews.find('a').text


print(MarsNewsTitle)

MarsDict={"Article_Title": MarsNewsTitle}

print(MarsDict)


# In[5]:


MarsTease = soup.find("div", class_="article_teaser_body").text


print(MarsTease)
MarsDict["Article_Tease"] = MarsTease


# In[6]:


# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a 
# variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[7]:


html = browser.html
soup = bs(html, 'html.parser')


# In[8]:


carousels = soup.find_all('article', class_='carousel_item')


# In[9]:


for carousel in carousels:
    article = carousel["style"]
    img_url = article.lstrip()   
    img_url = img_url.split()
    img_url = img_url[1]
    img = img_url[5:57]
print(img)

print(url[:24])


# In[10]:


main_img_url = url[:24] + img



print (main_img_url)

MarsDict["RecentMarsPic"] = main_img_url
    


# In[11]:


#Scrape Mars Weather Tweet
url = "https://twitter.com/marswxreport?lang=en"
browser.visit(url)


# In[12]:


# Scrape page into soup
html = browser.html
soup = bs(html, "html.parser")

MarsWTweet = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

print(MarsWTweet)
print(type(MarsWTweet))

MarsDict["Mars Weather"] = MarsWTweet

print(MarsDict)


# In[13]:


# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, 
#Mass, etc.
# Use Pandas to convert the data to a HTML table string.
import pandas as pd
url = 'https://space-facts.com/mars/'

tables = pd.read_html(url)
tables


# In[14]:


df =tables[0]

df.columns = ["", "values"]


# In[15]:


df.set_index("", inplace=True)

df.head()


# In[17]:


html_table = pd.DataFrame.to_html(df)

print(type(html_table))
html_table

MarsDict["Html_Table"]=html_table

MarsDict


# In[18]:


# Visit the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the 
# hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary 
# for each hemisphere.
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

mars_hemi = "Cerberus Hemisphere Enhanced"

browser.visit(url)


# In[19]:


browser.click_link_by_partial_text(mars_hemi)
    


# In[20]:


html = browser.html
soup = bs(html, "html.parser")

picdownload = soup.find('div', class_="downloads")

picdownload


# In[21]:



hemi_pic = picdownload.find('li')

hemi=hemi_pic.a["href"]
hemi


# In[22]:


image_url =[]
hemi_dict={}
hemi_dict["tile"]=mars_hemi
hemi_dict["img_url"]=hemi

image_url.append(hemi_dict)

image_url


# In[23]:


mars_hemis = ["Cerberus Hemisphere Enhanced","Schiaparelli Hemisphere Enhanced", "Syrtis Major Hemisphere Enhanced","Valles Marineris Hemisphere Enhanced"]
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


hemisphere_image_urls=[]

for mars_hemi in mars_hemis:
   
    browser.visit(url)

    browser.click_link_by_partial_text(mars_hemi)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    picdwnload = soup.find('div',class_="downloads" )
    
    hemi_url =picdwnload.find('li').a["href"]
    
    hemi_dict={}
    
    hemi_dict["title"]=mars_hemi
    
    hemi_dict["img_url"]=hemi_url
    
    hemisphere_image_urls.append(hemi_dict)
    
    

hemisphere_image_urls   



# hemisphere_image_urls = [
#     {"title": "", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
#     {"title": , "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
#     {"title": , "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
#     {"title": , "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
# ]


# In[140]:


MarsDict["Mars_Hemispheres"]=hemisphere_image_urls 

MarsDict 

