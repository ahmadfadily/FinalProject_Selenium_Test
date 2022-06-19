import time
from Confirmation import Code_checker
from Alert_Handling import Alert_Handler
from Log_Update import test_update
from Click_Handling import click_function

def Login(driver, Email,expected,test_name):
    #driver.get("http://localhost:63342/FinalProjectFrontEnd/Login/Login.html?_ijt=e9picq2g0bsv4pvm0nakafsfaq")
    driver.get("http://localhost:63342/FinalProjectFrontEnd/Login/Login.html")
    driver = click_function(driver,Email)
    time.sleep(1)
    if expected != "No Alert":
        Test_Output, alert = Alert_Handler(driver,expected)
        test_update(test_name, Test_Output)
    else:
        Code_checker(driver,Email)

