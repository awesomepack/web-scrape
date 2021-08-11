'''
Scrape.py contains functions used in the completion of Homework 12 Mission_To_Mars: Web Scraping
'''

# Defining the scrape function
def Scrape():
    '''
    Scrape retreives data from various mars mission websites and returns a dictionary containing the following structure:
    return_dict = {
        'news_title': news_title , 
        'news_p': news_p ,
        'f_img': img_url ,  
        'facts': facts_html , 
        'Hems': Hems
    }
    '''

    # Importing Dependencies
    from bs4 import BeautifulSoup as bs
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd

    # Setting up connection to chrome browser using splinter

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome' , **executable_path , headless = False)

    # Scraping the news title and its paragraph text from the Mars news site https://redplanetscience.com/
    news_target = 'https://redplanetscience.com/'
    browser.visit(news_target)

    news_html = browser.html # Storing the current browser's html page

    soup = bs(news_html , 'html.parser') # Creating soup object from html file

    # The title text we are interested in is in <div class = 'content_title'
    # We want the most recent title so we use the find() function
    news_title = soup.find('div' , class_ = 'content_title').text

    # The paragraph text we are interested in has class = 'article_teaser_body'
    news_p = soup.find('div' , class_ = 'article_teaser_body').text

    # Visiting the space image site 'https://spaceimages-mars.com/'
    image_target = 'https://spaceimages-mars.com/'
    browser.visit(image_target)
    image_html = browser.html
    news_soup = bs(image_html , 'html.parser')

    # Extracting the relative url of the featured image
    rel_url = news_soup.find('img' , class_ = 'headerimage').get('src')

    # Concatenating the root url with that of the imag url
    img_url = image_target + rel_url

    # Visiting the Mars Facts site 'https://galaxyfacts-mars.com/'
    facts_target = 'https://galaxyfacts-mars.com/'

    # Use pandas to scrape the html table of all the mars facts
    tables = pd.read_html(facts_target)

    # Slicing out the table we are interested in
    mars_facts = tables[0]

    # Displaying the mars_facts DF
    mars_facts.head()

    # Transforming the extracted table using pandas
    # Renaming the column names
    mars_facts.columns = ['Mars/Earth Comparison' , 'Mars' , 'Earth']

    # Dropping the first row in the data frame
    mars_facts.drop( axis= 0 , index = 0 , inplace=True)

    # Displaying the transformed Data Frame
    mars_facts.head()

    # Converting the pandas DF into html table
    facts_html = mars_facts.to_html()

    # Visiting Astropedia to scrape hemisphere images 'https://marshemispheres.com/'
    hem_target = 'https://marshemispheres.com/'
    browser.visit(hem_target)
    hem_html = browser.html
    hem_soup = bs(hem_html , 'html.parser')
    # Finding the links to the hemispheres in the landing page
    hem_links = browser.links.find_by_partial_text('Hemisphere')

    # Defining list to contain hemisphere dictionaries
    Hems = []

    # Looping through the links to the different hemispheres
    for link in range(0 , 4):

        # Finding the links to the hemispheres in the landing page
        hem_links = browser.links.find_by_partial_text('Hemisphere')

        # navigating to the page
        hem_links[link].click()

        # Receiving the html response
        html = browser.html

        # Generating soup object from html response
        soup = bs(html , 'html.parser')

        # Extracting hemisphere title
        title = soup.find_all('h2' , class_ = 'title')[0].text

        # Extracting imag url
        img = soup.find('img' , class_ = 'wide-image').get('src')
        

        # Defining hemisphere dictionary
        hem_dict = {
            'title': title ,
            'image_url': img
            }

        # Appending Hems list
        Hems.append(hem_dict)
        

        # Return to home page
        browser.links.find_by_partial_text('Back').click()

    
    # Populating return_dict with scraped data
    return_dict = {
        'news_title': news_title , 
        'news_p': news_p ,
        'f_img': img_url ,  
        'facts': facts_html , 
        'Hems': Hems
    }

    return return_dict
        

