import time
from Confirmation import Code_checker
from Alert_Handling import Alert_Handler
from Log_Update import test_update

#def Report_Click(driver,input):
#    while True:
#    	try:
#    		user = driver.find_element_by_xpath("/html/body/div/div/input")
#    		user.send_keys(input)
#    		user.send_keys(Keys.ENTER)
#    		time.sleep(1)
#    		user = driver.find_element_by_xpath("/html/body/div/div/a")
#    		Erorr_Handling(user)
#    		return driver
#    	except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
#    		print("stuck in exception : " + str(e))
#    		time.sleep(1)
#    return True



#def Counters(driver, Email,expected,test_name,Path):
#    driver = Report_Click(driver,Email,Path)
#    time.sleep(1)
#    if expected != "No Alert":
#        Test_Output, alert = Alert_Handler(driver,expected)
#        test_update(test_name, Test_Output)
#    else:
#        Code_checker(driver,Email)
#        print("write here the confirmation code test")
