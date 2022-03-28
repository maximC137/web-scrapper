#importing the required libraries
from urllib.request import urlopen

#webscraper for example to test the web scraping tool
url ="https://webscraper.io/test-sites/tables"
html_code =urlopen(url).read().decode("utf-8")
print(html_code)

#getting a specific html line like the heading tags
start =html_code.find("<h1") +len("<h1>")
end =html_code.find("</h1>")
print (html_code[start:end])