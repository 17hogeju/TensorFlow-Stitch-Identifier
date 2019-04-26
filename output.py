# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 14:14:59 2019

@author: 17hog
"""

import tkinter as tk
import tkinter.filedialog
import classify
#from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk



class Browse(tk.Frame):
    """ Creates a frame that contains a button when clicked lets the user to select
    a file and put its filepath into an entry.
    """
    

    def __init__(self, master, initialdir='', filetypes=()):
        super().__init__(master)
        self.filepath = tk.StringVar()
        self._initaldir = initialdir
        self._filetypes = filetypes
        self._create_widgets()
        self._display_widgets()
        self.filename = ""

    def _create_widgets(self):
        self._entry = tk.Entry(self, textvariable=self.filepath, width= 100)
        self._button = tk.Button(self, text="Browse...", command=self.browse)
        self._label = tk.Label(self, text = "Choose a picture to see the stitch type")


    def _display_widgets(self):
        self._label.pack(anchor = "n")
        self._button.pack(side = tk.RIGHT, padx = 10)
        self._entry.pack(side = tk.RIGHT)
        
        
    
    def browse(self):
        """ Browses a .png file or all files and then puts it on the entry.
        """
        filen = tk.filedialog.askopenfilename(initialdir=self._initaldir,filetypes=self._filetypes)
        self.filepath.set(filen)
        self.filename = filen

        
    def messageWindow(self):
        win = tk.Toplevel()
        frame = tk.Frame(win, width=200, height=50)
        win.title('Results test')
        global image2
        img=Image.open(self.filename)
        img2=img.resize((100,50),Image.ANTIALIAS) #make image smaller
        image2=ImageTk.PhotoImage(img2)
        panel = tk.Label(win, image = image2)
        panel.pack(anchor = "s")
        

        classify.test_function(self.filename)
        file1 = open("output.txt","r+") 

        mg = file1.read()
        message = "Stitch Percentages:\n %s" % mg
        tk.Label(win, text=message).pack()
        tk.Button(win, text='OK', command=win.destroy).pack()
        frame.pack()
        

    
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x400')

    file_browser = Browse(root, initialdir=r"C:\Users",filetypes=(("All files", "*.*"),('Portable Network Graphics','*.png')))
    
    file_browser.pack(fill='x', expand=True)
    tk.Button(root, text='Submit', command=file_browser.messageWindow).pack(anchor = 's', pady = 50)
    

    root.mainloop()