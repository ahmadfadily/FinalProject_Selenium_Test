import time
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException
from Confirmation import Code_checker
from Alert_Handling import Alert_Handler
from Log_Update import test_update
from Click_Handling import Erorr_Handling

def Report_Click(driver,path,expectedPath,expectedText,Report):
    user = driver.find_element_by_xpath(path)
    Erorr_Handling(user)
    time.sleep(4)
    counter = 0
    while True:
        if counter == 8:
            test_update(Report, False)
            break
        try:
            chwd = driver.window_handles
            driver.switch_to.window(chwd[1])
            time.sleep(1)
            user = driver.find_element_by_xpath(expectedPath)
            text = user.text
            test_update(Report,text == expectedText)
            if Report == "Abort Report":
                Aborts(driver,user)
            if Report =="PMs Report":
                PMs(driver,user)
            driver.close()
            driver.switch_to.window(chwd[0])
            break
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
            print(e)
            print("waiting for " + expectedText + " to show")
            counter+=1
            time.sleep(1)
    time.sleep(1)


def Aborts(driver,user):
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/h1/u")
    time.sleep(4)
    text = user.text
    test_update("Tracers Button", text == "Active Tracers")


def PMs(driver,user):
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div/button[1]")
    time.sleep(4)
    text = user.text
    test_update("Tracers Button", text == "PROM Filter")
    Erorr_Handling(user)
    time.sleep(2)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr/th[2]")
    text = user.text
    test_update("Prom Filter", text == "Sub Entity")
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button[2]")
    Erorr_Handling(user)

    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/button")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/table/tbody/tr/th[2]")
    text = user.text
    test_update("BGUIPAPumpChangePM", text == "Sub Entity")

    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button[4]")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[1]/div/button[2]")
    Erorr_Handling(user)
    user = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div[2]/table/tbody/tr/th[4]")
    text = user.text
    test_update("BGUG2LChamberSupercleanPM", text == "Checklist Open")

