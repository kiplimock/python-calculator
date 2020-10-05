from tkinter import *

root = Tk()
# application title
root.title('Python Calculator')
# make the window not resizable
root.geometry('300x400')


# an empty string to store the expression to be evaluated
text_input = StringVar()
expression = ""

# configure the row and column to be responsive to window size
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=50)

for i in range(5):
    root.rowconfigure(i, weight=1, minsize=30)

# the screen

screen = Entry(root, bg='#efefef', fg='#444', width = 15, font=('roboto', 18),\
                justify=RIGHT, textvariable=text_input)

screen.grid(columnspan=4, sticky='nesw')

# button definitions
btn_7 = Button(root, text='7', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('7')).grid(row=1, column=0, sticky='nesw')
btn_8 = Button(root, text='8', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('8')).grid(row=1, column=1, sticky='nesw')
btn_9 = Button(root, text='9', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('9')).grid(row=1, column=2, sticky='nesw')
btn_4 = Button(root, text='4', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('4')).grid(row=2, column=0, sticky='nesw')
btn_5 = Button(root, text='5', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('5')).grid(row=2, column=1, sticky='nesw')
btn_6 = Button(root, text='6', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('6')).grid(row=2, column=2, sticky='nesw')
btn_1 = Button(root, text='1', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('1')).grid(row=3, column=0, sticky='nesw')
btn_2 = Button(root, text='2', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('2')).grid(row=3, column=1, sticky='nesw')
btn_3 = Button(root, text='3', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('3')).grid(row=3, column=2, sticky='nesw')
btn_0 = Button(root, text='0', height=1, width=3, fg='#444', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('0')).grid(row=4, column=0, sticky='nesw')
btn_clear = Button(root, text='C', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_clear()).grid(row=4, column=1, sticky='nesw')
btn_equals = Button(root, text='=', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_equals()).grid(row=4, column=3, sticky='nesw')
add = Button(root, text='+', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('+')).grid(row=1, column=3, sticky='nesw')
subtract = Button(root, text='-', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('-')).grid(row=2, column=3, sticky='nesw')
multiply = Button(root, text=u'\u00D7', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('*')).grid(row=3, column=3, sticky='nesw')
divide = Button(root, text=u'\u00F7', height=1, width=3, fg='#e67e22', bg='#ccc', font=('roboto', 18), cursor="hand2",\
                command=lambda:btn_click('/')).grid(row=4, column=2, sticky='nesw')


# function definitions
def btn_click(number):
    global expression
    expression = expression + str(number)
    text_input.set(expression)

def btn_clear():
    global expression
    expression = ""
    screen.delete(0, END)

def btn_equals():
    global expression
    expression = screen.get()
    try:
        result = str(eval(expression))
        text_input.set(result)
        expression = ""
    except:
        text_input.set('Error')
        expression = ""
        

root.mainloop()