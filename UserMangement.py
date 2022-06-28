import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Alert_Handling import Alert_Handler
from Log_Update import test_update
from Click_Handling import Erorr_Handling


def UserManagement(driver):
    View_Users(driver)
    user_name = Add_Admin(driver)
    Remove_Admin(driver,user_name)
    View_Users(driver)
    #time.sleep(1)
    View_Admin(driver, user_name)
    #time.sleep(1)
    Add_New_User(driver,"Michael", "Bar-Sinai", "barsinam@post.bgu.ac.il")
    View_Users(driver)
    #time.sleep(2)
    Remove_User(driver,"Michael Bar-Sinai - MichaelBar-Sinai")
    View_Users(driver)
    #time.sleep(2)
    # its not showing in the remove user list because its already deleted
    test_update("Remove User",Remove_User(driver,"Michael Bar-Sinai - MichaelBar-Sinai") == False)
    #time.sleep(2)


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
    output,label_number = View_Admin(driver, user_name)
    if output:
        l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
        Erorr_Handling(l[label_number])
        user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
        Erorr_Handling(user)
        #now after we deleted the admin should be false :
        output = View_Admin(driver, user_name)
        if not output:
            test_update("Remove Admin", True)

def View_Admin(driver,user_name):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[4]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                test_update("Add Admin appears in Remove Admin", True)
                return True,label_number
            #print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)

def Add_New_User(driver,fname,lname,email):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[5]")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/input[1]")
    user.send_keys(fname)
    user.send_keys(Keys.ENTER)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/input[2]")
    user.send_keys(lname)
    user.send_keys(Keys.ENTER)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/input[3]")
    user.send_keys(email)
    user.send_keys(Keys.ENTER)
    time.sleep(1)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    time.sleep(1)
    test_update("Add User", True)


def Remove_User(driver,user_name):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[6]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == user_name:
                test_update("Add User appears in Remove User", True)
                l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
                Erorr_Handling(l[label_number])
                user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                Erorr_Handling(user)
                return True
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)
