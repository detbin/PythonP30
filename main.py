import tkinter
from tkinter import ttk
def reiniciar() :
    seleccion.set(None)
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=7)
window.columnconfigure(2, weight=5)
seleccion = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccion)
r2 = ttk.Radiobutton(window, text='No', value='2', variable=seleccion)
r3 = ttk.Radiobutton(window, text='No se', value='3', variable=seleccion)
r4 = ttk.Radiobutton(window, text='No quiero opinar', value='4', variable=seleccion)
r5= ttk.Button(window, text='Reiniciar', command=reiniciar)
r1.grid(row=0, column=0, sticky=tkinter.W, padx=5, pady=5)
r2.grid(row=1, column=0, sticky=tkinter.W, padx=5, pady=5)
r3.grid(row=2, column=1, sticky=tkinter.W, padx=5, pady=5)
r4.grid(row=3, column=1, sticky=tkinter.W, padx=5, pady=5)
r5.grid(row=4, column=2, sticky=tkinter.W, padx=5, pady=5)
window.mainloop()
window.quit()
