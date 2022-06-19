import time
from Confirmation import Code_checker
from Alert_Handling import Alert_Handler
from Log_Update import test_update
from Click_Handling import click_function

def Login(driver, Email,expected,test_name):
    driver.get("C:\\Users\\t-afadila\\WebstormProjects\\FinalProjectFrontEnd\\Login\\Login.html")
    driver = click_function(driver,Email)
    time.sleep(1)
    if expected != "No Alert":
        Test_Output, alert = Alert_Handler(driver,expected)
        test_update(test_name, Test_Output)
    else:
        Code_checker(driver,Email)
        print("write here the confirmation code test")

