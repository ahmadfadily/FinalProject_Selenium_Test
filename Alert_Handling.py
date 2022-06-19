from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException
from selenium.webdriver.common.alert import Alert

import time

def Alert_Accept(output,alert):
    timer = 0
    while True:
        try:
            alert.accept()
            return output, alert
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
            if timer == 5:
                return output, alert
            print("stuck in exception : " + str(e))
            time.sleep(1)
            timer += 1

def Alert_msg(alert, msg):
    if alert.text == msg:
        return Alert_Accept(True, alert)
    else:
        return Alert_Accept(False, alert)



def Alert_Handler(driver,msg):
    timer = 0
    while True:
        try:
            alert = Alert(driver)
            return Alert_msg(alert,msg)
        except (NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException) as e:
            if timer == 5:
                return False
            print("stuck in exception : " + str(e))
            time.sleep(1)
            timer += 1


