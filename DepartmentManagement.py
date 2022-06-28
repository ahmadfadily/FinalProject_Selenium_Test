import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Log_Update import test_update
from Click_Handling import Erorr_Handling
from Alert_Handling import Alert_Handler


def DepartmentManagement(driver):
    ViewMachines(driver)
    machine_name = RemoveMachines(driver)
    AddMachines(driver,machine_name)
    machine_name,attribute = AddMachineAttributes(driver)
    RemoveMachineAttributes(driver,machine_name,attribute)

def ViewMachines(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[14]")
    Erorr_Handling(user)
    test_update("View Machines", True)

    #user_list=driver.find_elements(By.CLASS_NAME, "report_card parent_entity_container")
    #if len(user_list) > 0 :
    #    test_update("View Machines",True)
    #else:
    #    test_update("View Machines",False)

def RemoveMachines(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[16]")
    Erorr_Handling(user)
    time.sleep(1)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    if len(l) > 0:
        n = len(l)-1
    else:
        return
    user_name = l[n].text
    Erorr_Handling(l[n])
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    time.sleep(1)
    test_update("Remove Machines Success Alert appeared",Alert_Handler(driver,"Success !"))
    return user_name


def AddMachines(driver,machine_name):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[15]")
    Erorr_Handling(user)
    time.sleep(1)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == machine_name:
                test_update("Remove Machine appears in Add Machines", True)
                Erorr_Handling(l[label_number])
                user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                Erorr_Handling(user)
                time.sleep(1)
                test_update("Add Machines Success Alert appeared", Alert_Handler(driver, "Success !"))
                return True,label_number
            #print(l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)


def AddMachineAttributes(driver):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[17]")
    Erorr_Handling(user)
    time.sleep(1)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    if len(l) > 0:
        n = len(l)-1
    else:
        return
    machine_name = l[len(l)-1].text
    Erorr_Handling(l[n])
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)

    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    if len(l) > 0:
        n = len(l)-1
    else:
        return
    attribute_name = l[len(l)-1].text
    Erorr_Handling(l[n])
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
    Erorr_Handling(user)
    time.sleep(1)
    test_update("Add Machines Attribute Success Alert Appeared", Alert_Handler(driver, "Success !"))
    return machine_name,attribute_name


def RemoveMachineAttributes(driver,machine_name,attribute_name):
    time.sleep(1)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[18]")
    Erorr_Handling(user)
    l = driver.find_elements(By.CLASS_NAME, "checkbox_container")
    test_update("Remove Attribute",True)
    try:
        label_number = 0
        while label_number in range(0, len(l)):
            if l[label_number].text == machine_name:
                #print(l[label_number].text)
                Erorr_Handling(l[label_number])
                user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                Erorr_Handling(user)
                attribute_number = 0
                time.sleep(1)
                #while attribute_number in range(0, len(l[label_number])):
                #    if l[label_number][attribute_number].text == attribute_name:
                #        print(l[label_number][attribute_number].text)
                #        test_update("Add Attribute appears in Remove Attribute ", True)
                #        Erorr_Handling(l[label_number][attribute_number])
                #        user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/button")
                #        Erorr_Handling(user)
                #        test_update("Remove Attribute Alert Appeared", Alert_Handler(driver, "Success !"))
                #    else:
                #        label_number+=1
                #return True
            #print("else ", l[label_number].text)
            label_number += 1
        return False
    except(NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
        print(e)

