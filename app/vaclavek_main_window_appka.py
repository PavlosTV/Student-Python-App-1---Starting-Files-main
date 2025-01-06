### GUI imports
from guizero import *
from vaclavek_main_appka import *

def cml1():
    hmotnost = float(txtbox_weight.value)
    af=float(txtbox_af.value)
    cml=cml2(hmotnost, af)
    return cml

### GUI functions
def my_first_gui_function():
    text_welcome.value = "Ahoj, uživateli!"
    cmltxt = cml1()
    text_cml.value = f"tvoje cml je {cmltxt}"


### GUI App
app = App(title="My App", width=775, height=650)

## Window 1
window1 = Box(app, visible=True)

# Welcome text
text_welcome = Text(window1, text=(f"Hi, user!"))

# Input activity factor
text_af = Text(
    window1,
    text=(
        "        Please enter your activity factor for today:"
    )
)
txtbox_af = TextBox(window1)

# Input weight
text_weight = Text(
    window1,
    text=(f"Please enter your weight in kilograms (kg):")
)
txtbox_weight = TextBox(window1)

# Output calorie maintenance level
text_cml = Text(window1, text ="")

# Display an image
image_widget = Picture(
    window1,
    image="resources/images/calculating_cml.png",
    width=680,
    height=480,
    align="bottom"
)

#button
button = PushButton(window1, command=my_first_gui_function)

app.display()

