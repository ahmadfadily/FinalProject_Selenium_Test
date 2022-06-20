import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from Log_Update import test_update
from Click_Handling import Erorr_Handling
from PermissionManagement import PermissionManagement
from UserMangement import UserManagement
from selenium.webdriver.common.by import By

from Alert_Handling import Alert_Handler
from selenium.webdriver.common.alert import Alert

def Control(driver,path,expectedPath,expectedText,Task):
    user = driver.find_element_by_xpath(path)
    Erorr_Handling(user)
    counter = 0
    while True:
        if counter == 5:
            test_update(Task, False)
            break
        try:
            chwd = driver.window_handles
            driver.switch_to.window(chwd[1])
            time.sleep(1)
            user = driver.find_element_by_xpath(expectedPath)
            text = user.text
            test_update(Task,text == expectedText)
            UserManagement(driver)
            #PermissionManagement(driver)
            driver.close()
            driver.switch_to.window(chwd[0])
            break
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
            print("waiting for " + expectedText + " to show")
            counter+=1
            time.sleep(1)
    time.sleep(1)
