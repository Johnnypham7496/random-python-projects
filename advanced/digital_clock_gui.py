# Now let’s see how to create a digital clock GUI application with Python. I will first start with importing the libraries:
from tkinter import Label, Tk
import time


# Now let’s define the title and size of our application. 
# Note that in the code below I will set both the height and width of the resizable function as True(1,1) 
# if you want a fixed window and don’t want to maximize or minimize the output you can set it to False(0,0):
app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("370x150")
app_window.resizable(0,0)

# Now here I will define the font of the time and its colour
# its border width and the background colour of the digital clock:
text_font = ("Calibri", 68, 'bold')
background_color = "#000000"
foreground_color = "#FFFFFF"
border_width = 25


# Now here I will combine all the elements to define the label of the clock application:
label = Label(app_window, font= text_font, bg= background_color, fg= foreground_color, bd= border_width)
label.grid(row= 0, column= 1)


# Now let’s define the main function of our digital clock. Here I will set the text of the label as the realtime:
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)


# Now let’s run and see our output:
digital_clock()
app_window.mainloop()