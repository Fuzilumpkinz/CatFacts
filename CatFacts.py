# https://catfact.ninja/fact
#API result example
#{'fact': 'The most expensive cat was an Asian Leopard cat (ALC)-Domestic Shorthair (DSH) hybrid named Zeus. Zeus, who is 90% ALC and 10% DSH, has an asking price of £100,000 ($154,000).'
#, 'length': 175}


import requests
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__() #Super allows access to parent class
        self.title("Cat Facts!")
        self.geometry("600x200")
        self.buttonFact = tk.StringVar() #Have to use special var type with ktinker to edit labels
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=150)
        self.columnconfigure(2, minsize=150)
        self.columnconfigure(3, minsize=150)
        #API Location
        self.api_url = "https://catfact.ninja/fact"
        #Create objects in GUI
        self.createObjects()


    def catFact(self):
        response = requests.get(self.api_url)
        self.fact = response.json()["fact"]
        return self.fact

    def createObjects(self):
        #Label for catfact
        padding = {'padx': 5, 'pady': 5}
        
        self.buttonFact.set(self.catFact())
        self.output_label = ttk.Label(self, text=self.buttonFact.get(), wraplength=600)
        self.output_label.grid(column=0, row=0, **padding, columnspan=4)

        # Button - New Cat Fact
        catFact_button = ttk.Button(self, text='New Cat Fact!', command=self.submit)
        catFact_button.grid(column=1, row=4, **padding)

        # Button - Exit
        exit_button = ttk.Button(self, text='Exit', command=self.destroy)
        exit_button.grid(column=2, row=4, **padding)
        
    def submit(self):
        #Call catfact and update label
        self.buttonFact.set(self.catFact())
        self.output_label.config(text=self.buttonFact.get())
        

if __name__ == "__main__":
    root = App()
    root.mainloop()