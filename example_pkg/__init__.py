import sys
import datetime 
import calendar 

class Convert:

    def find_day(self, date): 
        born = datetime.datetime.strptime(date, '%d-%m-%Y').weekday() 
        return calendar.day_name[born]