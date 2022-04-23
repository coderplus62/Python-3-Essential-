import tkinter

# Initialize
main_window = tkinter.Tk()

# Label
label_1 = tkinter.Label(main_window, text="lable 1")
label_2 = tkinter.Label(main_window, text="lable 2")

# Button
button_1 = tkinter.Button(main_window, text="button 1")
button_2 = tkinter.Button(main_window, text="button 2")

# positioning methods
label_1.pack()
label_2.pack()
button_1.pack()
button_2.pack()

# display methods
main_window.mainloop()