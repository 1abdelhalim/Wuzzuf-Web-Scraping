# Wuzzuf-Web-Scraping
This Python script is designed to scrape job listings from the Wuzzuf job portal website using the requests and BeautifulSoup libraries. The script extracts job titles, company names, job locations, required skills, job links and job types from the Wuzzuf search results page, cleans and preprocesses the data, and saves it in a CSV file on the desktop


## Getting Started
To run this script, make sure you have Python 3 and the required libraries (requests, BeautifulSoup, csv, itertools) installed on your system. You can install the required libraries using pip by running the following command in your terminal:
pip install requests BeautifulSoup4 csv itertools

## Usage 
Open your terminal and navigate to the directory where you saved the wuzzuf.py file.
Run the script using the following command:
python wuzzuf.py
Once the script is executed successfully, it will create a CSV file named wuzzuf.csv on your desktop.


## Customization
You can customize this script to scrape job listings based on your specific search criteria by modifying the URL in the requests.get() method on line 11.
results = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python%20developer')

Replace python%20developer with your desired search query.

You can also modify the CSV file name and destination path by changing the path in the open() method on line 29
with open('desktop/wuzzuf.csv', 'w') as jobs:

## Conclusion
This script provides an efficient and effective way to extract job listings from the Wuzzuf job portal website using Python. It can be customized to suit your specific needs and can be used as a starting point for more advanced web scraping projects.


