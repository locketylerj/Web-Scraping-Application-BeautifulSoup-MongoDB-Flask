
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


def chrome_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Start with a function called `scrape` 
# that will execute all of your scraping code and return one Python dictionary containing all of the scraped data.
def scrape():

    #Get the Latest Mars News Title
    browser = chrome_browser()

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    
    html = browser.html
    soup = bs(html, "html.parser")

    
    
    
    MarsNews = soup.find("div", class_="content_title")

    MarsNewsTitle = MarsNews.find('a').text

    MarsDict={"Article_Title": MarsNewsTitle}

    #Get the latest Mars News article teaser paragraph
    
    MarsTease = soup.find("div", class_="article_teaser_body").text

    MarsDict["Article_Tease"] = MarsTease

    
    # Visit the next Url and get the main featured image full size image url 
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url2)
    html = browser.html

    soup = bs(html, 'html.parser')
    
    carousels = soup.find_all('article', class_='carousel_item')
    for carousel in carousels:
        article = carousel["style"]
        img_url = article.lstrip()   
        img_url = img_url.split()
        img_url = img_url[1]
        img = img_url[5:57]
    
    main_img_url = url2[:24] + img


    MarsDict["RecentMarsPic"] = main_img_url

    #Visit the twitter url and get the most recent weather data on Mars

    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)


    html = browser.html
    soup = bs(html, "html.parser")

    MarsWTweet = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    MarsDict["Mars_Weather"] = MarsWTweet

    #Get the Mars Facts table from the space facts website and put it into an html table string

    url4 = 'https://space-facts.com/mars/'

    tables = pd.read_html(url4)
    
    
    df =tables[0]

    df.columns = ["", "values"]

    df.set_index("", inplace=True)

    mars_html_table = pd.DataFrame.to_html(df)

    MarsDict["Html_Table"] = mars_html_table

    #Visit the 5th url and get image urls for each of the full size mars hemisphere pictures and put into mars dictionary
    mars_hemis = ["Cerberus Hemisphere Enhanced","Schiaparelli Hemisphere Enhanced", "Syrtis Major Hemisphere Enhanced","Valles Marineris Hemisphere Enhanced"]
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    hemisphere_image_urls=[]

    for mars_hemi in mars_hemis:
   
        browser.visit(url5)

        browser.click_link_by_partial_text(mars_hemi)
        
        html = browser.html
        soup = bs(html, "html.parser")
        
        picdwnload = soup.find('div',class_="downloads" )
        
        hemi_url =picdwnload.find('li').a["href"]
        
        hemi_dict={}
        
        hemi_dict["title"]=mars_hemi
        
        hemi_dict["img_url"]=hemi_url
        
        hemisphere_image_urls.append(hemi_dict)

    MarsDict["Mars_Hemispheres"]=hemisphere_image_urls 

    return MarsDict




