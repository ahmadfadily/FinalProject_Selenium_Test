import time

from Login import Login
from Reports import Report_Click

def Choosing_Cases(driver):

    # Tests :
    # Wrong Email Alert Check
    Login(driver,'intel.com',"Please enter valid email address", "Wrong Email Alert Check") #good

    #Tests :
    # NoneExisting Email, Null Conformation Code
    # Wrong Email, Wrong Conformation Code
    # Right Email, Right Conformation Code
    Login(driver,'tamer.nassar@intel.com', "No Alert", "Right Email Check")

    #Tests :
    # Counter Report
    Report_Click(driver,"/html/body/div[3]/div[1]/div[2]","/html/body/div[2]/div[1]/h2","CleanPM","Counter Report")

    # Tests :
    # Chemical Report
    Report_Click(driver, "/html/body/div[3]/div[1]/div[3]", "/html/body/div[2]/div[1]/span/b", "PROM - BGUcp", "Chemical Report")

    # Tests :
    # Entered Abort Report
    # Tracers Work
    Report_Click(driver, "/html/body/div[3]/div[1]/div[4]", "/html/body/div[2]/div/button[2]", "Tracers", "Abort Report")

    # Tests :
    # PMs Report
    # Tracers Work
    Report_Click(driver, "/html/body/div[3]/div[1]/div[5]", "/html/body/div[2]/div[1]/div/button[1]", "Filter PMs", "PMs Report")

