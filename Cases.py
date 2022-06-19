from Login import Login

def Choosing_Cases(driver):

    Login(driver,'intel.com',"Please enter valid email address", "Wrong Email Alert Check") #good
    Login(driver,'tamer.nassar@intel.com', "No Alert", "Right Email Check") #passes
    


