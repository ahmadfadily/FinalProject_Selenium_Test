import time
from selenium.webdriver import Keys
from Pull_Data import Confirmation_Code, Full_Name
from Log_Update import test_update
from Alert_Handling import Alert_Handler
from Click_Handling import click_function

def User_Entered(driver,email):
    user = driver.find_element_by_xpath("/html/body/div[2]/div[1]/span")
    #test_update("Right Email, Right Conformation Code", user.text == Full_Name(email))
    test_update("Right Email, Right Conformation Code", user.text == "Group 20")
    time.sleep(3)

def Code_checker(driver, email):
    # NoneExisting email test
    test_update("NoneExisting Email, Null Conformation Code", Confirmation_Code('s') == []  )

    # Wrong email test
    code = Confirmation_Code('ahmad.fadila@mock.com')
    driver = click_function(driver,code)
    output = Alert_Handler(driver, "Wrong confirmaion")
    test_update("Wrong Email, Wrong Conformation Code", output)
    time.sleep(1)
    Alert_Handler(driver,'s')
    time.sleep(1)


    #print(Confirmation_Code(Email))  # right email, wrong confirmation code

    code = Confirmation_Code(email)  # right email, right confirmation code
    driver = click_function(driver,code)
    User_Entered(driver,email)
