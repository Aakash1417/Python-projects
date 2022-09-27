import tkinter as tk

root = tk.Tk()
root.title("Calculator")

xPad = 25

buttons = []

EnteredText = tk.StringVar()
EnteredText.set("0")
operator = ''

e = tk.Entry(root, width=30, text=EnteredText, bg="white", borderwidth=5,
             justify="right").grid(columnspan=4, padx=10, pady=10)


def butClick(num):
    global operator
    operator = operator + str(num)
    EnteredText.set(operator)


def clearBox():
    global operator
    operator = ''
    EnteredText.set("")


def stripZeros(string):
    temp = string.split("+")
    if len(temp) == 2:
        if temp[0][0] == "0":
            temp[0] = temp[0][1:len(temp[0])]
        if temp[1][0] == "0":
            temp[1] = temp[1][1:len(temp[1])]
        return temp[0] + "+" + temp[1]
    temp = string.split("-")
    if len(temp) == 2:
        if temp[0][0] == "0":
            temp[0] = temp[0][1:len(temp[0])]
        if temp[1][0] == "0":
            temp[1] = temp[1][1:len(temp[1])]
        return temp[0] + "-" + temp[1]
    temp = string.split("/")
    if len(temp) == 2:
        if temp[0][0] == "0":
            temp[0] = temp[0][1:len(temp[0])]
        if temp[1][0] == "0":
            temp[1] = temp[1][1:len(temp[1])]
        return temp[0] + "/" + temp[1]
    temp = string.split("*")
    if len(temp) == 2:
        if temp[0][0] == "0":
            temp[0] = temp[0][1:len(temp[0])]
        if temp[1][0] == "0":
            temp[1] = temp[1][1:len(temp[1])]
        return temp[0] + "*" + temp[1]


def evaluateAns():
    global operator
    operator = EnteredText.get()
    operator = str(eval(stripZeros(operator)))
    EnteredText.set(operator)


def delete():
    global operator
    x = slice(0, len(operator) - 1, 1)
    operator = operator[x]
    EnteredText.set(operator)

def invoke_button(row,col, text):
    tk.Button(root, padx=xPad, pady=xPad / 2, text=text, command=lambda: butClick(text), activebackground="darkgrey").grid(
        row=row, column=col)


invoke_button(2,0,7)
invoke_button(2,1,8)
invoke_button(2,2,9)

invoke_button(2,0,7)
invoke_button(2,1,8)
invoke_button(2,2,9)

invoke_button(3,0,4)
invoke_button(3,1,5)
invoke_button(3,2,6)

# invoke_button(2,0,7)
# invoke_button(2,0,7)

# tk.Button(root, padx=xPad, pady=xPad/2, text=7, command=lambda: butClick(7), activebackground="darkgrey").grid(row=2, column=0)
# tk.Button(root, padx=xPad, pady=xPad/2, text=8, command=lambda: butClick(8), activebackground="darkgrey").grid(row=2, column=1)
# tk.Button(root, padx=xPad, pady=xPad/2, text=9, command=lambda: butClick(9), activebackground="darkgrey").grid(row=2, column=2)

tk.Button(root, padx=xPad, pady=xPad/2, text=4, command=lambda: butClick(4), activebackground="darkgrey").grid(row=3, column=0)
tk.Button(root, padx=xPad, pady=xPad/2, text=5, command=lambda: butClick(5), activebackground="darkgrey").grid(row=3, column=1)
tk.Button(root, padx=xPad, pady=xPad/2, text=6, command=lambda: butClick(6), activebackground="darkgrey").grid(row=3, column=2)

tk.Button(root, padx=xPad, pady=xPad/2, text=1, command=lambda: butClick(1), activebackground="darkgrey").grid(row=4, column=0)
tk.Button(root, padx=xPad, pady=xPad/2, text=2, command=lambda: butClick(2), activebackground="darkgrey").grid(row=4, column=1)
tk.Button(root, padx=xPad, pady=xPad/2, text=3, command=lambda: butClick(3), activebackground="darkgrey").grid(row=4, column=2)
tk.Button(root, padx=xPad, pady=xPad/2, text=0, command=lambda: butClick(0), activebackground="darkgrey").grid(row=5, column=1)

tk.Button(root, padx=xPad, pady=xPad/2, text="/", bg="grey", command=lambda: butClick("/"), activebackground="darkgrey").grid(row=1, column=1)
tk.Button(root, padx=xPad, pady=xPad/2, text="X", bg="grey", command=lambda: butClick("*"), activebackground="darkgrey").grid(row=1, column=2)
tk.Button(root, padx=xPad, pady=xPad/2, text="+", bg="grey", command=lambda: butClick("+"), activebackground="darkgrey").grid(row=3, column=3)
tk.Button(root, padx=xPad, pady=(xPad/2)+4, height=4, text="=", bg="blue", command=evaluateAns, activebackground="darkblue").grid(row=4, column=3, rowspan=2)
tk.Button(root, padx=xPad, pady=xPad/2, text="C", bg="grey", command=clearBox, activebackground="darkgrey").grid(row=1, column=0)
tk.Button(root, padx=xPad, pady=xPad/2, text="-", bg="grey", command=lambda: butClick("-"), activebackground="darkgrey").grid(row=2, column=3)
tk.Button(root, padx=xPad, pady=xPad/2, width=1, text="DEL", bg="grey", command=delete, activebackground="darkgrey").grid(row=1, column=3)
tk.Button(root, padx=xPad, pady=xPad/2, text=".", command=lambda: butClick("."), activebackground="darkgrey").grid(row=5, column=2)

root.mainloop()
