import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import UserMangement
from Log_Update import test_update
from Click_Handling import Erorr_Handling

def PermissionManagement(driver):
    UserMangement.Add_New_User(driver,"Ahmad","Fadila","afadila@microsoft.com")
    View_Users_Permission(driver, "Ahmad Fadila")
    user_name = Add_Machine_Management(driver)
    Remove_Machine_Management(driver,user_name)
    test_update("Remove Machine Management", View_Machine_Management(driver, user_name))
    user_name = Add_View_Report_Permission(driver)
    Remove_View_Report_Permission(driver,user_name)
    test_update("Remove View Report Permission",View_Report_Permission(driver,user_name))

def View_Users_Permission(driver,full_name):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[8]")
    Erorr_Handling(user)
    user_list=driver.find_elements(By.CLASS_NAME, "tablinks")
    #print(user[1].text)
    for n in range(0,len(user_list)):
        if user_list[n].text == full_name:
            Erorr_Handling(user_list[n])
            time.sleep(2)
            test_update("Viewing User Permissions", True)


def Add_Machine_Management(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[9]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    if len(l) > 0:
        n = len(l)-1
    else:
        return
    user_name = l[n].text
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/label[1]/span")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    return user_name

def Remove_Machine_Management(driver,user_name):
    print("View Machine Management")
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[10]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                test_update("Add Machine Management appears in Remove Machine Management", True)
                Erorr_Handling(l[label_number])
                user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                Erorr_Handling(user)
                return True,label_number
            print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)


def View_Machine_Management(driver, user_name):
    print("View Machine Managment")
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[9]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                return True
            print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)


def Add_View_Report_Permission(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[11]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    if len(l) > 0:
        n = len(l)-1
    else:
        return
    user_name = l[n].text
    Erorr_Handling(l[n])
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    return user_name


def Remove_View_Report_Permission(driver,user_name):
    print("View Machine Management")
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[12]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                test_update("Add View Report Permission appears in Remove Report Permission", True)
                Erorr_Handling(l[label_number])
                user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                Erorr_Handling(user)
                return True,label_number
            print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)


def View_Report_Permission(driver, user_name):
    print("View Report Permission")
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[11]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                return True
            print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)
