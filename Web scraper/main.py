from urllib.request import urlopen
from bs4 import BeautifulSoup

# This is a program to convert web information from a website and convert it to a csv file

# make a url variable (string) and insert the page url you desire to scrape
Url_to_scrape = "https://unicorncards.co.uk/yugioh-starter-and-structure-decks"

# Use urlopen function to request the page
page_request = urlopen(Url_to_scrape)

# Read the HTML RESPONSE using the .read() function
page_html = page_request.read()

# Close the response after reading it and saving it to a variable
page_request.close()

# Use BeautifulSoup to pick out the desired data from the HTML RESPONSE
html_soup = BeautifulSoup(page_html, 'html.parser')

# Use inspect element to find the class the desired data is stored in
card_items = html_soup.find_all('div', class_="product-item")

# Preparation to write to a csv
filename = 'Unicorn_cards.csv'
f = open(filename, 'w')

# create headers for the csv (end in a new line because it's a csv)
headers = 'Title, Price \n'

# Write the headers
f.write(headers)

# Use a for loop to run through each iteration of the class
for item in card_items:

    # Find the values stored within each iteration of the class (find function must end with .text)
    #(use the top left cursor icon and left click to narrow down the search)

    # The first argument passed in is based on the preceeding HTML tag which in this case is a <h2>
    title_pre_strip = item.find('h2', class_= 'product-title').text
    title = title_pre_strip.strip('\n')

    
    price_pre_strip = item.find('div', class_= 'prices').text
    price = price_pre_strip.strip('\n')


    # Write the information into the csv (concatenate a comma because it's a csv)
    f.write(title + ',' + price + '\n')

# End the for loop and close the file
f.close()

#the strip method was used due to the scraped data having enter spaces which caused a bug when displaying the csv file. this bug will be dependant on the data scraped and was fixed by trial and error.



