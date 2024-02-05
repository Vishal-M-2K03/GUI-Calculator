#import the tkinter module
from tkinter import *

#declaring the variable which handles the input and output in the text field
expression = ""

#function when button is clicked
def press(item):
    global expression
    expression = expression + str(item)
    equation.set(expression)

#function when clear button is cilcked
def btn_clear():
    global expression
    expression = ""
    equation.set(expression)

#function when equal button is cilcked
def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        expression = ""
        equation.set(result)
    except:
        btn_clear()
        equation.set("ERROR")
        expression = ""

#creating the main window
win = Tk()

#setting the height and width to the window
win.geometry("312x324")
win.resizable(0,0)

#title for the window
win.title("Calculator")

#input and output handling variable
equation = StringVar()

#creating a frame which has the entry to display all operators and operands
input_frame = Frame(win, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black",highlightthickness = 2)
input_frame.pack(side = TOP)

#creating a entry field to enter the operators and operands when corresponding button is clicked
input_field = Entry(input_frame, font = ('arial',18,'bold'), textvariable = equation, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0,column = 0)
input_field.pack(ipady = 10)

#creating an another frame which contains all buttons
btns_frame = Frame(win, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()

#Buttons 
#first row
clear = Button(btns_frame,text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda : btn_clear()).grid(row = 0,column = 0,columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame,text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2",command= lambda : press("/")).grid(row = 0, column = 3,padx = 1,pady = 1)

#second row
seven = Button(btns_frame, text = "7", fg = "black",width = 10, height = 3,  bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

#third row
four = Button(btns_frame, text = "4", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

#fourth row
one = Button(btns_frame, text = "1", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

#fifth row
zero = Button(btns_frame, text = "0", fg = "black",width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(0)).grid(row = 4, column = 0,columnspan = 2 ,padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :press(".")).grid(row = 4, column = 2,padx = 1, pady = 1)
equal = Button(btns_frame, text = "=", fg = "black",width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2",command=lambda :btn_equal()).grid(row = 4, column = 3,padx = 1, pady = 1)

#running the main window unitl we can close it manually
win.mainloop()