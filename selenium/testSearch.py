import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

searchName = "Keith"

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5000')

time.sleep(5)

search_box = driver.find_element_by_name('firstname')
search_box.send_keys(searchName)

time.sleep(5)
search_box.submit()

searchResultsTable = driver.find_element_by_id('searchResults')
searchResults = searchResultsTable.find_elements_by_tag_name('tr')

for row in searchResults:
	firstName = row.find_elements_by_tag_name('td')[1]
	if firstName.text != searchName:
		print "Error: a first name (" + firstName.text + ") presented does not match the search name!"
	else:
		print "Success: found matching name - " + firstName.text + " - ID = " + id.text


	

time.sleep(10)

driver.quit()
