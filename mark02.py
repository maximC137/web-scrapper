#importing the required libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

url ="https://webscraper.io/test-sites/tables"
html_code =urlopen(url).read().decode("utf-8")

#here we are going to install a parser ,maybe html parser of lxml
soup =BeautifulSoup(html_code ,'lxml')
heading_2 =soup.find_all("h2")
print(heading_2)

#let us try to find images
images =soup.find_all("img")
print(images)
#to get the source and the alternative one of the first image we type
print(images[1]['src'])
print(images[1]['alt'])

#to find a table and exclude the heading 
first_table =soup.find('table')
rows =first_table.findAll('tr')[1:]
last_names =[]
for row in rows :
	last_names.append(row.findAll('td')[2])
print (last_names)
#to remove the <td></td> tags we use
for row in rows :
	last_names.append(row.findAll('td')[2].get_text())
print (last_names)