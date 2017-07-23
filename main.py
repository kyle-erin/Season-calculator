from time import gmtime, strftime
import math
from collections import OrderedDict

currentmonth = str(strftime("%B")) 
currentdate = int(strftime("%d"))

#totaldaysinsummer
totaldays = 93
currentdays = 0

#summer starts on june 20th so there are 10 days of summer in june
#summer ends on september 21st so there are 21 days of summer in september
daysofsummer = OrderedDict([('June', 10), ('July', 31), ('August', 31), ('September', 21)])

for k, v in daysofsummer.items():
	if k != currentmonth:
		currentdays += v
	else:
		currentdays += currentdate
		break 

percentin = round((currentdays / totaldays) * 100, 2)
print('We are ' + str(percentin) + "% through summer! " + str(100. - percentin) + '% ' + 'left! There are ' + str(totaldays - currentdays) + ' days left of summer and ' +  str(currentdays) + ' days have passed since the beginning of summer.')
