from tkinter import *  #tkinter is used for making gui apps in python
import random #random package is used similarly as the randomize function in c
import time #time package is used for accessing time values to display

root = Tk() #iniitalizing window component
root.geometry("1600x8000") #dimensions
root.title("Restaurant Management") #title bar

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

#time display
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="SHADES RESTAURANT", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0) #app label

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0) #time label

lblInfo2 = Label(Tops, font=('arial', 20, 'bold'), text='', fg="Red", bd=10, anchor='w')
lblInfo2.grid(row=2, column=0) #error label only shown when error is generated



def Ref(): #function used for calculation of bill
    global randomRef, CoFries, CostofFries, CoNoodles, CostofNoodles, CoSoup, CostofSoup, CoBurger, CostBurger
    global CoSandwich, CostSandwich, CoD, CostofDrinks, TotalCost, Ser_Charge, PayTax, TotalCost, AllCost
    #global declaration of variables allows us to access them in other blocks of code

    #reference no. generation
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    try: #try block
        if (Fries.get() == ""):  #if user doesnt enter a quantity of fooditem it will be attained a value of 0
            CoFries = 0
        else:
            CoFries = float(Fries.get()) #else it attains the provided value

        if (Noodles.get() == ""):
            CoNoodles = 0
        else:
            CoNoodles = float(Noodles.get())

        if (Soup.get() == ""):
            CoSoup = 0
        else:
            CoSoup = float(Soup.get())

        if (Burger.get() == ""):
            CoBurger = 0
        else:
            CoBurger = float(Burger.get())

        if (Sandwich.get() == ""):
            CoSandwich = 0
        else:
            CoSandwich = float(Sandwich.get())

        if (Drinks.get() == ""):
            CoD = 0
        else:
            CoD = float(Drinks.get())

    except ValueError: #the except[read catch in languages] for cactching value error occured
        lblInfo2.config(text="Invalid values, please re-enter")

    CostofFries = CoFries * 140 #calculation of costs of food items and other calculations based on it
    CostofDrinks = CoD * 65
    CostofNoodles = CoNoodles * 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger * 260
    CostSandwich = CoSandwich * 300

    CostofMeal = "Rs", str(
        '%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich))

    PayTax = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.09)

    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.09)

    GST = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    AllCost = PayTax + TotalCost + Ser_Charge

    GST_Charge.set(GST) #attaining values to suitable labels
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def saveData(): #function using file handling to write data of bill generated by applicaiton in a text file
    with open("rstmgt.txt", "a") as f:
        f.write('\nBill reference number = ' + randomRef)
        f.write('\nFries * %.2f = Rs %.2f' %(CoFries,CostofFries))
        f.write('\nNoodles * %.2f = Rs %.2f' %(CoNoodles,CostofNoodles))
        f.write('\nSoup * %.2f = Rs %.2f' %(CoSoup,CostofSoup))
        f.write('\nBurger * %.2f = Rs %.2f' %(CoBurger,CostBurger))
        f.write('\nSandwich * %.2f = Rs %.2f' %(CoSandwich,CostSandwich))
        f.write('\nDrinks * %.2f = Rs %.2f' %(CoD,CostofDrinks))
        f.write('\nCost of Meal = Rs %.2f' %TotalCost)
        f.write('\nGST = Rs %.2f' %Ser_Charge)
        f.write('\nSGST = Rs %.2f' %PayTax)
        f.write('\nSub Total = Rs %.2f' %TotalCost)
        f.write('\nTotal Cost = Rs %.2f' %AllCost)
        f.write('\n')

def checkData(): #function using file handling to read data of bill text file
    with open("rstmgt.txt", "r") as f:
        print(f.read())


def qExit(): #function for exiting app
    root.destroy()


def Reset(): #function for clearing entries{textboxes}
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    GST_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")


#info left
rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
SubTotal = StringVar()
Total = StringVar()
GST_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Burger = StringVar()
Sandwich = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtFries.grid(row=1, column=1)

lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtNoodles.grid(row=2, column=1)

lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtSoup.grid(row=3, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtBurger.grid(row=4, column=1)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSandwich.grid(row=5, column=1)


#info right
lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Drinks", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtCost.grid(row=1, column=3)

lblGST = Label(f1, font=('arial', 16, 'bold'), text="GST", bd=16, anchor="w")
lblGST.grid(row=2, column=2)
txtGST = Entry(f1, font=('arial', 16, 'bold'), textvariable=GST_Charge, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtGST.grid(row=2, column=3)

lblSGST = Label(f1, font=('arial', 16, 'bold'), text="SGST", bd=16, anchor="w")
lblSGST.grid(row=3, column=2)
txtSGST = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSGST.grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtTotalCost.grid(row=5, column=3)

# buttons
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="powder blue", command=Ref).grid(row=7, column=1)

btnSave = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Save",
                  bg="powder blue", command=saveData).grid(row=7, column=2)

btnHistory = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="History",
                  bg="powder blue", command=checkData).grid(row=7, column=3)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="powder blue", command=Reset).grid(row=7, column=4)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="powder blue", command=qExit).grid(row=7, column=5)

root.mainloop()


