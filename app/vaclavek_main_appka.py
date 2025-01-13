# Importing all app imports
from vaclavek_config_appka import *

# Main Window Functions

def cml2(hmotnost, af):
        bmr=hmotnost*24.2
        cml=round(bmr*af,2)
        return cml

def group(pohlavi):
        if pohlavi =="muž":
                return "ahoj chlape"
        elif pohlavi =="žena":
                return "ahoj ženo"
        elif pohlavi =="jiné":
                return "ahoj"
        

                
# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries
