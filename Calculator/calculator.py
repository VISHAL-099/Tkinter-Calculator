from tkinter import*

 #define the button(btn)click function

def btnclick(numbers):  
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

 # define the clear function

def btnClearDisplay():  
    global operator
    operator=""
    text_Input.set("")

 #define the Equal to function

def btnEqualsInput():   
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operators=""

 # name the app, i choose a "Calculator" because it's random

cal = Tk()
cal.title("GUI Calculator")      
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input,bd=5,insertwidth=30,fg="black",
                   bg="white", justify='right').grid(columnspan=20) 
btnclear=Button(cal,padx=18,pady=5,bd=1, fg="black",font=('arial', 20,'bold'),
            text="C",bg="red",command=btnClearDisplay).grid(row=1,column="0")

BtnM=Button(cal,padx=18,pady=5,bd=1, fg="black",font=('arial', 20,'bold'),
            text="M",bg="yellow",).grid(row=1,column="1")

Btnbraket1=Button(cal,padx=26,pady=6,bd=1, fg="black",font=('arial', 20,'bold'),
            text="(",bg="powder blue",command=lambda:btnclick("(")).grid(row=1,column="2")

Btnbracket2=Button(cal,padx=26,pady=8,bd=1, fg="black",font=('arial', 18,'bold'),
            text=")",bg="powder blue",command=lambda:btnclick(")")).grid(row=1,column="3")
#=======================================================================================================================

btn7=Button(cal,padx=22,pady=14,bd=0, fg="black",font=('arial', 20,'bold'),
            text="7",bg="white",command=lambda:btnclick(7)).grid(row=2,column="0")

btn8=Button(cal,padx=22,pady=14,bd=0, fg="black",font=('arial', 20,'bold'),
            text="8", bg="white",command=lambda:btnclick(8)).grid(row=2,column="1")

btn9=Button(cal,padx=22,pady=14,bd=0, fg="black",font=('arial', 20,'bold'),
            text="9", bg="white",command=lambda:btnclick(9)).grid(row=2,column="2")

Division=Button(cal,padx=24,pady=12,bd=1, fg="black",font=('arial', 18,'bold'),
            text="/",bg="powder blue",command=lambda:btnclick("/")).grid(row=5,column="2")
#===========================================================================================================================

btn6=Button(cal,padx=22,pady=13,bd=0, fg="black",font=('arial', 20,'bold'),
            text="6",bg="white",command=lambda:btnclick(6)).grid(row=3,column="0")

btn5=Button(cal,padx=22,pady=13,bd=0, fg="black",font=('arial', 20,'bold'),
            text="5",bg="white",command=lambda:btnclick(5)).grid(row=3,column="1")

btn4=Button(cal,padx=22,pady=13,bd=0, fg="black",font=('arial', 20,'bold'),
            text="4",bg="white",command=lambda:btnclick(4)).grid(row=3,column="2")

subtraction=Button(cal,padx=26,pady=15,bd=1, fg="black",font=('arial', 18,'bold'),
            text="-",bg="powder blue",command=lambda:btnclick("-")).grid(row=3,column="3")
#===============================================================================================================================

btn3=Button(cal,padx=22,pady=18,bd=0, fg="black",font=('arial', 20,'bold'),
            text="3",bg="white",command=lambda:btnclick(3)).grid(row=4,column="0")

btn2=Button(cal,padx=22,pady=18,bd=0, fg="black",font=('arial', 20,'bold'),
            text="2",bg="white",command=lambda:btnclick(2)).grid(row=4,column="1")

btn1=Button(cal,padx=22,pady=18,bd=0, fg="black",font=('arial', 20,'bold'),
            text="1",bg="white",command=lambda:btnclick(1)).grid(row=4,column="2")

Multiplication=Button(cal,padx=25,pady=17,bd=1, fg="black",font=('arial', 18,'bold'),
            text="*",bg="powder blue",command=lambda:btnclick("*")).grid(row=4,column="3")
#==================================================================================================================================
Dot=Button(cal,padx=22,pady=12,bd=1, fg="black",font=('arial', 18,'bold'),
            text=".",bg="blue",command=lambda:btnclick(".")).grid(row=5,column="0")

Btn0=Button(cal,padx=22,pady=12,bd=1, fg="black",font=('arial', 20,'bold'),
            text="0",bg="white",command=lambda:btnclick(0)).grid(row=5,column="1")



Equal=Button(cal,padx=22,pady=12,bd=1, fg="black",font=('arial', 18,'bold'),
            text="=",bg="green",command=btnEqualsInput).grid(row=5,column="3")

Addition=Button(cal,padx=23,pady=14,bd=1, fg="black",font=('arial', 18,'bold'),
            text="+",bg="powder blue",command=lambda:btnclick("+")).grid(row=2,column="3")



cal.mainloop()
