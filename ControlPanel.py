import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from Log_Update import test_update
from Click_Handling import Erorr_Handling
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
            if Task == "Control Panel":
                UserManagement(driver)
            if Task == "Remove User":
                driver.close()
                driver.switch_to.window(chwd[0])
            break
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
            print("waiting for " + expectedText + " to show")
            counter+=1
            time.sleep(1)
    time.sleep(1)

def UserManagement(driver):
    View_Users(driver)
    user_name = Add_Admin(driver)
    Remove_Admin(driver,user_name)

def View_Users(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div")
    text = user.get_attribute("id")
    test_update("View Users", text == "organization_chart")

def Add_Admin(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]")
    Erorr_Handling(user)
    user = driver.find_element(By.CLASS_NAME,"checkbox_container")
    user_name = user.text
    user = driver.find_element(By.CLASS_NAME,"checkmark")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    time.sleep(2)
    output = Alert_Handler(driver, "Success !")
    test_update("Add Admin", output)
    return user_name


def Remove_Admin(driver,user_name):
    l = driver.find_elements(By.CLASS_NAME, "checkmark")
    for i in l:
        print("here")
        print(i)
        print(i.element)
        Erorr_Handling(i)