# Importing all app imports
from vaclavek_config_appka import *

# Main Window Functions

def cml2(hmotnost, af):
        bmr=hmotnost*24.2
        cml=bmr*af
        cml=round(cml,2)
        return cml


# Main Window Variables
todays_date_str = dt.date.today().strftime("%d-%m-%Y") #this is a string
todays_date_obj = dt.date.today() #this is an object

# Main Window Lists / Dictionaries
