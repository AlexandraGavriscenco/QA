from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.instagram.com/")

driver.maximize_window()


e = 'text@yahoo.com'
p = 'parola123'


email = driver.find_element_by_xpath(
    "//*[@id='loginForm']/div/div[1]/div/label/input")
email.send_keys(e)


password = driver.find_element_by_xpath(
    "//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys(p)
