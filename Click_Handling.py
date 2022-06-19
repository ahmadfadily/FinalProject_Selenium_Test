from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
import time
from selenium.webdriver import Keys

def Erorr_Handling(user):
	while True:
		try:
			user.click()
			break
		except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
			print("stuck in exception : " + str(e))
			time.sleep(1)


def click_function(driver,input):
	while True:
		try:
			user = driver.find_element_by_xpath("/html/body/div/div/input")
			user.send_keys(input)
			user.send_keys(Keys.ENTER)
			time.sleep(1)
			user = driver.find_element_by_xpath("/html/body/div/div/a")
			Erorr_Handling(user)
			return driver
		except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
			print("stuck in exception : " + str(e))
			time.sleep(1)

