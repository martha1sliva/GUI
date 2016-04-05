from Tkinter import *

import random
 
class Application(Frame):
    
    def __init__(self,master):
        Frame.__init__(self, master)
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        #creating top label
        self.lbl_design = Label(self, text = "Calculate Your Airfaire").grid(row = 0, column = 1, columnspan = 1)
        #creating customer label and entry box
        self.lbl_name = Label(self, text = "Customer Name:").grid(row = 1, column = 0, sticky = E)
        self.entry_name = Entry(self, width = 40)
        self.entry_name.grid(row = 1,column = 1, columnspan = 1)
        #options label
        self.lbl_options = Label(self, text = "Select Your Options:").grid(row = 2, column = 1, columnspan=1)
        #choose class label and radios
        self.lbl_class=Label(self, text="Choose Class:").grid(row=3, column=0)
        self.select_class = StringVar()
        self.select_class.set("Economy(baseline)")
        Radiobutton(self, text = "Economy(baseline)",variable = self.select_class, value = "economy").grid(row =  4, column = 0, sticky = W)
        Radiobutton(self, text = "Business(50% more)", variable = self.select_class, value = "business").grid(row =  5, column = 0, sticky = W)
        Radiobutton(self, text = "Luxury(200% more)",variable = self.select_class, value = "luxury").grid(row =  6, column = 0, sticky = W)
        #choose airline label and radios
        self.lbl_airline=Label(self, text="Choose Airline:").grid(row=3, column=1)
        self.select_airline = StringVar()
        self.select_airline.set("Delta(1 dollar per mile)")
        Radiobutton(self, text = "Delta(1 dollar per mile)",variable = self.select_airline, value = "Delta").grid(row =  4, column = 1)
        Radiobutton(self, text = "United(80 cents per mile)", variable = self.select_airline, value = "United").grid(row =  5, column = 1)
        Radiobutton(self, text = "Southwest(60 cents per mile)",variable = self.select_airline, value = "Southwest").grid(row=6, column=1)
        Radiobutton(self, text = "JetBlue(50 cents per mile)",variable = self.select_airline, value = "JetBlue").grid(row =  7, column = 1)
        #choose extras label and checkboxes
        self.lbl_extras = Label(self, text = "Inflight Extras:").grid(row = 3, column = 2)
        self.headphones = BooleanVar()
        self.beverage = BooleanVar()
        self.peanuts = BooleanVar()
        Checkbutton(self, text = "Headphones($4)", variable = self.headphones).grid(row = 4, column = 2)
        Checkbutton(self, text = "Beverage($10)", variable = self.beverage).grid(row = 5, column = 2)
        Checkbutton(self, text = "Peanuts($40)", variable = self.peanuts).grid(row = 6, column = 2)
        #input distance traveled label and entry box
        self.lbl_name = Label(self, text = "Distance Traveled(miles):").grid(row = 8, column = 0)
        self.ent = Entry(self, width = 15)
        self.ent.grid(row = 9,column = 0)
        #calculate button
        self.bttn = Button(self, text = "Calculate!", command= self.update_text).grid(row = 9, column = 2)
        #empty text box
        self.text_box = Text(self, width = 90, height = 5, wrap = WORD)
        self.text_box.grid(row = 10, column = 0, columnspan = 3)

    def update_text(self):
        #updates the text with name box and chosen radiobuttons
        message = "Thanks for flying with us, "
        name = self.entry_name.get()
        message += name + "."
        message += "\nYou've selected a "
        class_type = self.select_class.get()
        message += class_type
        message += " class flight on "
        airline = self.select_airline.get()
        message += airline
        message += " airlines"

        #updates text with checked boxes
        if self.headphones.get() and self.beverage.get() and self.peanuts.get():
            message += " with headphones, a beverage, and peanuts"
        elif self.headphones.get() and self.beverage.get():
            message += " with headphones and a beverage"
        elif self.headphones.get() and self.peanuts.get():
            message += " with headphones and peanuts"
        elif self.beverage.get() and self.peanuts.get():
            message += " with a beverage and peanuts"
        elif self.headphones.get():
            message += " with headphones"
        elif self.beverage.get():
            message += " with a beverage"
        elif self.peanuts.get():
            message += " with peanuts"
        message += "."

        #calculates total
        total = 0
        fees = 0
        try:
            distance = float(int(self.ent.get()))
            
            if airline == "Delta":
                total+= distance
            elif airline == "United":
                total+=distance*.8
            elif airline == "Southwest":
                total+=distance*.6
            elif airline == "JetBlue":
                total+=distance*.5

            if self.headphones.get():
                total+=4
            if self.beverage.get():
                total+=10
            if self.peanuts.get():
                total+=50

            if class_type == "economy":
                total = total
            elif class_type == "business":
                total = total*(1.5)
            elif class_type == "luxury":
                total = total*2

            message += "\nYour total comes to $" + str(total)
            
            #calculating total with tax and fees
            total += total*.07
            fees += (distance/100)*20

            total += fees

            message += "\nWith 7% tax plus $" + str(fees) + " your true final cost will be $" + str(total)
            
        except:
            message += "\nSorry, this is an invalid distance."


        
        #updates the text boxes in the program
        self.entry_name.delete(0,END)
        self.entry_name.insert(0, "")
        self.ent.delete(0, END)
        self.ent.insert(0,"")
        self.text_box.delete(0.0, END)
        self.text_box.insert(0.0, message)        
        

root = Tk()
root.title("Airfare Estimator")
#root.geometry("650x350")
root.resizable(width = False, height = False)
app = Application(root)
root.mainloop()
