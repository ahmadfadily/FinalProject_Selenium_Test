import time
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from colorama import Fore

def test_update(test_name, output):
	f=open('Logfile/Logfile.txt', 'a')
	if output:
		f.write(test_name + ' ---> ')
		f.write('Succeeded, ')
		f.write(str(datetime.now()) + '\n')
	else:
		f.write(test_name + ' ---> ')
		f.write('Failed, ')
		f.write(str(datetime.now()) + '\n')

	f.close()
	time.sleep(1)