from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble
from insertion_sort import insertion

root = Tk()
root.title("Sorting Visualizer")
root.maxsize(900, 600)
root.config(bg="black")

data = []
select_alg = StringVar()  # Define select_alg as a global variable

def generate():
    global data
    minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    sizeval = int(sizeEntry.get())
    data = [random.randint(minval, maxval) for _ in range(sizeval)]
    drawData(data, ['red' for _ in range(len(data))])

def drawData(data, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width / (len(data) + 1)
    offset = 30
    spacing = 10

    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = can_height - height * 340
        x1 = (i + 1) * x_width + offset
        y1 = can_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0 + 2, y0, anchor=SE, text=str(data[i]))
    root.update_idletasks()

def start_algorithm():
    global data
    algorithm = select_alg.get()
    if algorithm == "Bubble Sort":
        bubble(data, drawData, speedbar.get())
    elif algorithm == "Insertion Sort":
        insertion(data, drawData, speedbar.get())

Mainframe = Frame(root, width=600, height=200, bg="grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(Mainframe, text="SORTING ALGORITHM", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)

algmenu = ttk.Combobox(Mainframe, textvariable=select_alg, values=["Bubble Sort", "Insertion Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(0)

Button(Mainframe, text="START", bg="blue", command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)

speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)

sizeEntry = Scale(Mainframe, from_=3, to=60, resolution=1,
                  orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(Mainframe, from_=0, to=10, resolution=1,
                 orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(Mainframe, from_=10, to=100, resolution=1,
                 orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(Mainframe, text="Generate", bg="red", command=generate).grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
