import sys
import datetime 
import calendar 

class Date_convert:

    #program_name = sys.argv[0]
    #arguments = sys.argv[1:]
    def __init__(self):
        pass

    def findDay(self, date): 
        born = datetime.datetime.strptime(date, '%d-%m-%Y').weekday() 
        return (calendar.day_name[born]) 
  
#print(findDay(ddate)) 