import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import UserMangement
from Log_Update import test_update
from Click_Handling import Erorr_Handling

def PermissionManagement(driver):
    #UserMangement.Add_New_User(driver,"Ahmad","Fadila","afadila@microsoft.com")
    View_Users_Permission(driver, "Ahmad Fadila")


def View_Users_Permission(driver,full_name):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]")
    Erorr_Handling(user)
    user_list ="/html/body/div[2]/div[2]/div[1]/div/button["
    user_number = 1
    button = user_list + str(user_number) +"]"
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/button[2]")
    Erorr_Handling(user)
    print(user.text)
    #print("View_Users_Permission")
    #for user in range(0,len(user_list)):
    #    print(user_list[user].text)
    #    if user_list[user].text == full_name:
    #        user_list = driver.find_elements(By.CLASS_NAME, "tablinks")
    #        Erorr_Handling(user_list[user])
    #        try:
    #            permission_shown = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[6]/table/tbody/tr/th[1]")
    #            test_update("View Users Permission", True)
    #        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
    #            test_update("View Users Permission", False)
#
