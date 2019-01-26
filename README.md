# Mission to Mars

![mission_to_mars](Images/mission_to_mars.jpg)

Web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Step 1 - Scraping

Initial web scraping is done using a Jupyter Notebook, BeautifulSoup, Pandas,and Requests/Splinter.

* Jupyter Notebook file called `mission_to_mars.ipynb` used to complete all of the scraping and analysis tasks. 

### NASA Mars News

* Scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) and collects the latest News Title and Paragraph Text. Assigns the text to variables that you can reference later.

```python
# Example:
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Visits the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Uses splinter to navigate the site and find the image url for the current Featured Mars Image and assigns the url string to a variable called `featured_image_url`.

* Saves a complete url string for this image.

```python
# Example:
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
```

### Mars Weather

* Visits the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrapes the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called `mars_weather`.

```python
# Example:
mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'
```

### Mars Facts

* Visits the Mars Facts webpage [here](http://space-facts.com/mars/) and uses Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

* Uses Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visits the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Each of the links to the hemispheres are clicked on in order to find the image url to the full resolution image.

* Saves both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Uses a Python dictionary to store the data using the keys `img_url` and `title`.

* Appends the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.

```python
# Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

## Step 2 - MongoDB and Flask Application

MongoDB with Flask templating are used to create an HTML page that displays all of the information that was scraped from the URLs above.

* Inital jupyter notebook is converted into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.

* A route called `/scrape` imports the `scrape_mars.py` script and calls the `scrape` function.

  * Stores the return value in Mongo as a Python dictionary.

* The root route `/` queries the Mongo database and passes the mars data into an HTML template to display the data.

* The template HTML file called `index.html` takes the mars data dictionary and displays all of the data in the appropriate HTML elements. The following is a guide for what the final product should look like.

![final_app_part1.png](Images/final_app_part1.png)
![final_app_part2.png](Images/final_app_part2.png)

- - -
To run application locally: 
1. Download all files. 
2. Open MongoDB and connect to proper route. 
3. In GitBash enter: source activate pythondata.
4. Use GitBash to navigate to the file location
5. Enter python MarsApp.py in Gitbash
6. In browser enter localhost:5000

## Additional Notes

* Splinter is used to navigate the sites when needed and BeautifulSoup is used to help find and parse out the necessary data.

* Pymongo for CRUD applications is used for the database. Overwrites the existing document each time the `/scrape` url is visited and new data is obtained.

* Uses Bootstrap to structure the HTML template.

