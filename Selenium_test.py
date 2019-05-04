# Import the necessary tools and open the website:
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/ChD/chromedriver.exe")
driver.implicitly_wait(10)    # Set the time to waiting for elements
driver.get("http://192.168.99.101:5000")    # Open the website
text = driver.find_element_by_xpath("//html/body")
new_text = str(text.text).replace(" World", " ")
print(new_text)
driver.quit()   # Close the window
