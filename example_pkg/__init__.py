import sys
import datetime 
import calendar 

class DateConvert:

    def find_day(self, date): 
        born = datetime.datetime.strptime(date, '%d-%m-%Y').weekday() 
        print(calendar.day_name[born]) 
        return calendar.day_name[born]