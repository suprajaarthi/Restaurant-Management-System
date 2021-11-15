from tkinter import *
import time
import random
import tkinter.messagebox
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import END





root =Tk()
root.geometry("1400x750+0+0")
root.title("Restaurant Billing System")
root.configure(background='lightcyan')

Tops = Frame(root, bd=25, pady=20, relief=GROOVE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 30, 'bold'), text='Restaurant Billing System', bd=15,
                fg='darkcyan', justify=CENTER)
lblTitle.grid(row=0)



ReceiptCal_Function = Frame(root, bd=10, relief=GROOVE)
ReceiptCal_Function.pack(side=LEFT)

Buttons_Function = Frame(ReceiptCal_Function, bd=3, relief=GROOVE)
Buttons_Function.pack(side=TOP)

Calculator_Function = Frame(ReceiptCal_Function,  bd=6, relief=GROOVE)
Calculator_Function.pack(side=BOTTOM)

Receipt_Function = Frame(ReceiptCal_Function,  bd=4, relief=GROOVE)
Receipt_Function.pack(side=BOTTOM)

MenuFrame = Frame(root,  bd=32, relief=GROOVE)
MenuFrame.pack(side=RIGHT)
Total_Function = Frame(MenuFrame, bg='azure', bd=4)
Total_Function.pack(side=BOTTOM)
Drinks_Function = Frame(MenuFrame,bg='azure',bd=4)
Drinks_Function.pack(side=TOP)


Drinks_Function = Frame(MenuFrame, bg='azure', bd=4, relief=GROOVE)
Drinks_Function.pack(side=LEFT)
Food_Function = Frame(MenuFrame, bg='azure', bd=4, relief=GROOVE)
Food_Function.pack(side=RIGHT)
# variables

variable1 = IntVar()
variable2 = IntVar()
variable3 = IntVar()
variable4 = IntVar()
variable5 = IntVar()
variable6 = IntVar()
variable7 = IntVar()
variable8 = IntVar()
variable9 = IntVar()
variable10 = IntVar()
variable11 = IntVar()
variable12 = IntVar()
variable13 = IntVar()
variable14 = IntVar()
variable15 = IntVar()
variable16 = IntVar()

Date_of_Order = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Total_of_Food = StringVar()
Total_of_Drinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

cocktail = StringVar()
iced_tea = StringVar()
hot_chocolate = StringVar()
orange_juice = StringVar()
milkshake = StringVar()
mountain_dew = StringVar()
soda = StringVar()
coke = StringVar()

fried_chicken = StringVar()
kare_kare = StringVar()
crispy_pasta = StringVar()
Chicken_Momos = StringVar()
Chicken_Noodles = StringVar()
Hamburger_ = StringVar()
Frankie_ = StringVar()
chicken_Rice = StringVar()

cocktail.set("0")
iced_tea.set("0")
hot_chocolate.set("0")
orange_juice.set("0")
milkshake.set("0")
mountain_dew.set("0")
soda.set("0")
coke.set("0")

fried_chicken.set("0")
kare_kare.set("0")
crispy_pasta.set("0")
Chicken_Momos.set("0")
Chicken_Noodles.set("0")
Hamburger_.set("0")
Frankie_.set("0")
chicken_Rice.set("0")

Date_of_Order.set(time.strftime("%y/%m/%d"))

# Function Declaration

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def iSave():
    my_str1=textReceipt.get("1.0",END)  # read from one text box t1
    fob=filedialog.asksaveasfile(filetypes=[('text file','*.txt')],
        defaultextension='.txt',initialdir='D:\\my_data\\my_html',
        mode='w')
    try:
        fob.write(my_str1)
        fob.close()
        t1.delete('1.0',END) # Delete from position 0 till end 
        t1.update()  
        b1.config(text="Saved")
        b1.after(3000, lambda: b1.config(text='Save'))
    except :
        print ("Bill Generated Successfully !!!")

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    Total_of_Food.set("")
    Total_of_Drinks.set("")
    ServiceCharge.set("")
    textReceipt.delete("1.0", END)


    cocktail.set("0")
    iced_tea.set("0")
    hot_chocolate.set("0")
    orange_juice.set("0")
    milkshake.set("0")
    mountain_dew.set("0")
    soda.set("0")
    coke.set("0")

    fried_chicken.set("0")
    kare_kare.set("0")
    crispy_pasta.set("0")
    Chicken_Momos.set("0")
    Chicken_Noodles.set("0")
    Hamburger_.set("0")
    Frankie_.set("0")
    chicken_Rice.set("0")

    variable1.set(0)
    variable2.set(0)
    variable3.set(0)
    variable4.set(0)
    variable5.set(0)
    variable6.set(0)
    variable7.set(0)
    variable8 .set(0)
    variable9 .set(0)
    variable10 .set(0)
    variable11 .set(0)
    variable12 .set(0)
    variable13 .set(0)
    variable14 .set(0)
    variable15 .set(0)
    variable16 .set(0)


    textCocktail.configure(state=DISABLED)
    textIcedTea.configure(state=DISABLED)
    textHotChocolate.configure(state=DISABLED)
    textOrangeJuice.configure(state=DISABLED)
    textMilkShake.configure(state=DISABLED)
    textMountainDew.configure(state=DISABLED)
    textSoda.configure(state=DISABLED)
    textCoke.configure(state=DISABLED)
    textFriedChicken.configure(state=DISABLED)
    textKareKAre.configure(state=DISABLED)
    textCrispyPasta.configure(state=DISABLED)
    textChickenMomos.configure(state=DISABLED)
    textChickenNoodles.configure(state=DISABLED)
    textHamburger.configure(state=DISABLED)
    textFrankie.configure(state=DISABLED)
    textChickenRice.configure(state=DISABLED)

def TotalofUnit():
    Unit1 = float(cocktail.get())
    Unit2 = float(iced_tea.get())
    Unit3 = float(hot_chocolate.get())
    Unit4 = float(orange_juice.get())
    Unit5 = float(milkshake.get())
    Unit6 = float(mountain_dew.get())
    Unit7 = float(soda.get())
    Unit8 = float(coke.get())

    Unit9 = float(fried_chicken.get())
    Unit10 = float(kare_kare.get())
    Unit11 = float(crispy_pasta.get())
    Unit12 = float(Chicken_Momos.get())
    Unit13 = float(Chicken_Noodles.get())
    Unit14 = float(Hamburger_.get())
    Unit15 = float(Frankie_.get())
    Unit16 = float(chicken_Rice.get())

    Prices_Drinks = (Unit1 * 50) + (Unit2 * 45) + (Unit3 * 60) + (Unit4 * 35) + (Unit5 * 70) + (Unit6 * 40) + (Unit7 * 55) + (Unit8 * 75)

    Prices_Food = (Unit9 * 490) + (Unit10 * 450) + (Unit11 * 350) + (Unit12 * 400) + (Unit13 * 500) + (Unit14 * 250) + (Unit15 * 650) + (Unit16 * 370)



    DrinksPrices = "P" + str('%.2f' % Prices_Drinks)
    FoodsPrices = "P" + str('%.2f' % Prices_Food)
    Total_of_Food.set(FoodsPrices)
    Total_of_Drinks.set(DrinksPrices)
    SC = "P" + str('%.2f' % 2)
    ServiceCharge.set(SC)

    Sub_Total_of_Unit = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 2))
    SubTotal.set(Sub_Total_of_Unit)

    Tax = "P" + str('%.2f'%((Prices_Drinks + Prices_Food + 2) * 0.2))
    PaidTax.set(Tax)

    TT = ((Prices_Drinks + Prices_Food + 2) * 0.2)
    TC = "P" + str('%.2f'%(Prices_Drinks + Prices_Food + 2 + TT))
    TotalCost.set(TC)


def drinksCocktail():
    if variable1.get() == 1:
        textCocktail.configure(state=NORMAL)
        textCocktail.focus()
        textCocktail.delete('0', END)
        cocktail.set("")
    elif variable1.get() == 0:
        textCocktail.configure(state=DISABLED)
        cocktail.set("0")

def drinksIceTea():
    if variable2.get() == 1:
        textIcedTea.configure(state=NORMAL)
        textIcedTea.focus()
        textIcedTea.delete('0', END)
        iced_tea.set("")
    elif variable2.get() == 0:
        textIcedTea.configure(state=DISABLED)
        iced_tea.set("0")

def drinksHotChocolate():
    if variable3.get() == 1:
        textHotChocolate.configure(state=NORMAL)
        textHotChocolate.delete('0', END)
        textHotChocolate.focus()
    elif variable3.get() == 0:
        textHotChocolate.configure(state=DISABLED)
        hot_chocolate.set("0")

def drinksOrangeJuice():
    if variable4.get() == 1:
        textOrangeJuice.configure(state=NORMAL)
        textOrangeJuice.delete('0', END)
        textOrangeJuice.focus()
    elif variable4.get() == 0:
        textOrangeJuice.configure(state=DISABLED)
        orange_juice.set("0")

def drinksMilkShake():
    if variable5.get() == 1:
        textMilkShake.configure(state=NORMAL)
        textMilkShake.delete('0', END)
        textMilkShake.focus()
    elif variable5.get() == 0:
        textMilkShake.configure(state=DISABLED)
        milkshake.set("0")

def drinksMountainDew():
    if variable6.get() == 1:
        textMountainDew.configure(state=NORMAL)
        textMountainDew.delete('0', END)
        textMountainDew.focus()
    elif variable6.get() == 0:
        textMountainDew.configure(state=DISABLED)
        mountain_dew.set("0")

def drinksSoda():
    if variable7.get() == 1:
        textSoda.configure(state=NORMAL)
        textSoda.delete('0', END)
        textSoda.focus()
    elif variable7.get() == 0:
        textSoda.configure(state=DISABLED)
        soda.set("0")

def drinksCoke():
    if variable8.get() == 1:
        textCoke.configure(state=NORMAL)
        textCoke.delete('0', END)
        textCoke.focus()
    elif variable8.get() == 0:
        textCoke.configure(state=DISABLED)
        coke.set("0")

def foodsFriedChicken():
    if variable9.get() == 1:
        textFriedChicken.configure(state=NORMAL)
        textFriedChicken.delete('0', END)
        textFriedChicken.focus()
    elif variable9.get() == 0:
        textFriedChicken.configure(state=DISABLED)
        fried_chicken.set("0")

def foodsKareKare():
    if variable10.get() == 1:
        textKareKAre.configure(state=NORMAL)
        textKareKAre.delete('0', END)
        textKareKAre.focus()
    elif variable10.get() == 0:
        textKareKAre.configure(state=DISABLED)
        kare_kare.set("0")

def foodsCrispyPasta():
    if variable11.get() == 1:
        textCrispyPasta.configure(state=NORMAL)
        textCrispyPasta.delete('0', END)
        textCrispyPasta.focus()
    elif variable11.get() == 0:
        textCrispyPasta.configure(state=DISABLED)
        crispy_pasta.set("0")

def foodsChickenMomos():
    if variable12.get() == 1:
        textChickenMomos.configure(state=NORMAL)
        textChickenMomos.delete('0', END)
        textChickenMomos.focus()
    elif variable12.get() == 0:
        textChickenMomos.configure(state=DISABLED)
        Chicken_Momos.set("0")

def foodsChickenNoodles():
    if variable13 .get() == 1:
        textChickenNoodles.configure(state=NORMAL)
        textChickenNoodles.delete('0',END)
        textChickenNoodles.focus()
    elif(variable13.get() == 0):
        textChickenNoodles.configure(state=DISABLED)
        Chicken_Noodles.set("0")

def foodsHamburger():
    if variable14 .get() == 1:
        textHamburger.configure(state=NORMAL)
        textHamburger.delete('0', END)
        textHamburger.focus()
    elif variable14.get() == 0:
        textHamburger.configure(state=DISABLED)
        Hamburger_.set("0")

def foodsFrankie():
    if variable15.get() == 1:
        textFrankie.configure(state=NORMAL)
        textFrankie.delete('0', END)
        textFrankie.focus()
    elif variable15.get() == 0:
        textFrankie.configure(state=DISABLED)
        Frankie_.set("0")

def foodsChickenRice():
    if variable16 .get() == 1:
        textChickenRice.configure(state=NORMAL)
        textChickenRice.delete('0',END)
        textChickenRice.focus()
    elif(variable16.get() == 0):
        textChickenRice.configure(state=DISABLED)
        chicken_Rice.set("0")

def Receipt():
    textReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("Bill" + randomRef)

    textReceipt.insert(END, '*****************************************************************************'+'\n')

    textReceipt.insert(END, '\tBILL GENERATED:\t\t\t'+Receipt_Ref.get() + '\t' + Date_of_Order.get() + '\n')
    textReceipt.insert(END, '*****************************************************************************' +'\n')
    textReceipt.insert(END, 'Unit\t\t\t\t'+"Total of Unit \n")
    textReceipt.insert(END, 'Cocktail:\t\t\t\t\t' + cocktail.get() + '\n')
    textReceipt.insert(END, 'Iced Tea:\t\t\t\t\t' + iced_tea.get()+'\n')
    textReceipt.insert(END, 'Hot Chocolate:\t\t\t\t\t' + hot_chocolate.get()+'\n')
    textReceipt.insert(END, 'Orange Juice:\t\t\t\t\t' + orange_juice.get()+'\n')
    textReceipt.insert(END, 'Milk Shake:\t\t\t\t\t' + milkshake.get()+'\n')
    textReceipt.insert(END, 'Mountain Dew:\t\t\t\t\t' + mountain_dew.get()+'\n')
    textReceipt.insert(END, 'Soda:\t\t\t\t\t' + soda.get()+'\n')
    textReceipt.insert(END, 'Coke:\t\t\t\t\t' + coke.get()+'\n')
    textReceipt.insert(END, 'Fried Chicken:\t\t\t\t\t' + fried_chicken.get()+'\n')
    textReceipt.insert(END, 'Kare Kare:\t\t\t\t\t' + kare_kare.get()+'\n')
    textReceipt.insert(END, 'Crispy Pasta:\t\t\t\t\t' + crispy_pasta.get()+'\n')
    textReceipt.insert(END, 'Chicken Momos:\t\t\t\t\t' + Chicken_Momos.get()+'\n')
    textReceipt.insert(END, 'Chicken Noodles:\t\t\t\t\t' + Chicken_Noodles.get()+'\n')
    textReceipt.insert(END, 'Hamburger :\t\t\t\t\t' + Hamburger_.get()+'\n')
    textReceipt.insert(END, 'Frankie :\t\t\t\t\t' + Frankie_.get()+'\n')
    textReceipt.insert(END, 'Chicken Rice:\t\t\t\t\t' + chicken_Rice.get()+'\n')
    textReceipt.insert(END, 'Total of Drinks:\t\t\t\t' + Total_of_Drinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    textReceipt.insert(END, 'Total of Foods:\t\t\t\t' + Total_of_Food.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    textReceipt.insert(END, 'Service Charge:\t\t\t\t' + ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


# Drinks
Cocktail = Checkbutton(Drinks_Function, text='Cocktail', variable=variable1, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksCocktail).grid(row=0, sticky=W)
IcedTea = Checkbutton(Drinks_Function, text='Iced Tea', variable=variable2, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksIceTea).grid(row=1, sticky=W)
HotChocolate = Checkbutton(Drinks_Function, text='Hot Chocolate', variable=variable3, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksHotChocolate).grid(row=2, sticky=W)
OrangeJuice = Checkbutton(Drinks_Function, text='Orange Juice', variable=variable4, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksOrangeJuice).grid(row=3, sticky=W)
MilkShake = Checkbutton(Drinks_Function, text='Milk Shake', variable=variable5, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksMilkShake).grid(row=4, sticky=W)
MountainDew = Checkbutton(Drinks_Function, text='Mountain Dew', variable=variable6, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksMountainDew).grid(row=5, sticky=W)
Soda = Checkbutton(Drinks_Function, text='Soda', variable=variable7, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
                    bg='azure', command=drinksSoda).grid(row=6, sticky=W)
Coke = Checkbutton(Drinks_Function, text='Coke', variable=variable8, onvalue=1, offvalue=0, font=('arial', 16, 'bold'),
bg='azure', command=drinksCoke).grid(row=7, sticky=W)
# Drink Entry

textCocktail = Entry(Drinks_Function, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable=cocktail)
textCocktail.grid(row=0,column=1)

textIcedTea = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=iced_tea)
textIcedTea.grid(row=1,column=1)

textHotChocolate = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=hot_chocolate)
textHotChocolate.grid(row=2,column=1)

textOrangeJuice= Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=orange_juice)
textOrangeJuice.grid(row=3,column=1)

textMilkShake = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=milkshake)
textMilkShake.grid(row=4,column=1)

textMountainDew = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=mountain_dew)
textMountainDew.grid(row=5,column=1)

textSoda = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=soda)
textSoda.grid(row=6,column=1)

textCoke = Entry(Drinks_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=coke)
textCoke.grid(row=7,column=1)
# Foods

FriedChicken = Checkbutton(Food_Function,text="Fried Chicken\t\t\t ",variable=variable9,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsFriedChicken).grid(row=0,sticky=W)
KareKare = Checkbutton(Food_Function,text="Kare kare",variable=variable10,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsKareKare).grid(row=1,sticky=W)
CrispyPasta = Checkbutton(Food_Function,text="Crispy Pasta ",variable=variable11,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsCrispyPasta).grid(row=2,sticky=W)
ChickenMomos = Checkbutton(Food_Function,text="Chicken Momos ",variable=variable12,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsChickenMomos).grid(row=3,sticky=W)
ChickenNoodles = Checkbutton(Food_Function,text="Chicken Noodles ",variable=variable13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsChickenNoodles).grid(row=4,sticky=W)
Hamburger = Checkbutton(Food_Function,text="Hamburger  ",variable=variable14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsHamburger).grid(row=5,sticky=W)
Frankie = Checkbutton(Food_Function,text="Frankie  ",variable=variable15,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsFrankie).grid(row=6,sticky=W)
ChickenRice = Checkbutton(Food_Function,text="Chicken Rice ",variable=variable16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='azure',command=foodsChickenRice).grid(row=7,sticky=W)

textFriedChicken=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=fried_chicken)
textFriedChicken.grid(row=0,column=1)

textKareKAre=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=kare_kare)
textKareKAre.grid(row=1,column=1)

textCrispyPasta=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED, textvariable=crispy_pasta)
textCrispyPasta.grid(row=2,column=1)

textChickenMomos=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Chicken_Momos)
textChickenMomos.grid(row=3,column=1)

textChickenNoodles=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Chicken_Noodles)
textChickenNoodles.grid(row=4,column=1)

textHamburger=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Hamburger_)
textHamburger.grid(row=5,column=1)

textFrankie=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=Frankie_)
textFrankie.grid(row=6,column=1)

textChickenRice=Entry(Food_Function,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,textvariable=chicken_Rice)
textChickenRice.grid(row=7,column=1)

# ToTal Cost
lblTotalofDrinks=Label(Total_Function,font=('arial',14,'bold'),text='Total of Drinks\t',bg='azure',fg='darkslategrey',justify=CENTER)
lblTotalofDrinks.grid(row=0,column=0,sticky=W)
textTotalofDrinks=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Drinks)
textTotalofDrinks.grid(row=0,column=1)

lblTotalofFood=Label(Total_Function,font=('arial',14,'bold'),text='Total of Foods  ',bg='azure',fg='darkslategrey',justify=CENTER)
lblTotalofFood.grid(row=1,column=0,sticky=W)
textTotalofFood=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=Total_of_Food)
textTotalofFood.grid(row=1,column=1)

lblServiceCharge=Label(Total_Function,font=('arial',14,'bold'),text='Service Charge',bg='azure',fg='darkslategrey',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
# Payment information

lblPaidTax=Label(Total_Function,font=('arial',14,'bold'),text='\tPaid Tax',bg='azure',bd=7,fg='darkslategrey',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
textPaidTax=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=PaidTax)
textPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Total_Function,font=('arial',14,'bold'),text='\tSub Total',bg='azure',bd=7,fg='darkslategrey',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
textSubTotal=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'), insertwidth=2,justify=RIGHT,textvariable=SubTotal)
textSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Total_Function,font=('arial',14,'bold'),text='\tTotal',bg='azure',bd=7,fg='darkslategrey',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
textTotalCost=Entry(Total_Function,bg='whitesmoke',bd=7,font=('arial',14,'bold'),insertwidth=2,justify=RIGHT,textvariable=TotalCost)
textTotalCost.grid(row=2,column=3)

# RECEIPT
textReceipt=Text(Receipt_Function,width=66,height=20,bg='whitesmoke',bd=4,font=('arial',14,'bold'))
textReceipt.grid(row=5,column=5)


# BUTTONS
buttonTotal=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Total',bg='darkslategrey',command=TotalofUnit).grid(row=0,column=0)
buttonReceipt=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Receipt',bg='darkslategrey',command=Receipt).grid(row=0,column=1)
buttonReset=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Reset',bg='darkslategrey',command=Reset).grid(row=0,column=2)
buttonsave=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=7,text='Generate Bill',bg='darkslategrey',command=iSave).grid(row=0,column=3)
buttonExit=Button(Buttons_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='Exit',bg='darkslategrey',command=iExit).grid(row=0,column=4)



# Calculator Display



def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




# Calculator
txtDisplay = Entry(Calculator_Function, width=45, bg='lightcyan', bd=4, font=('arial',12,'bold'), justify=RIGHT, textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

# CALCULATOR BUTTONS
button7=Button(Calculator_Function, padx=16, pady=1, bd=7, fg='gold', font=('arial', 12, 'bold'), width=4, text='7',bg='darkslategrey',command=lambda:btnClick(7)).grid(row=2,column=0)
button8=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='8',bg='darkslategrey',command=lambda:btnClick(8)).grid(row=2,column=1)
button9=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='9',bg='darkslategrey',command=lambda:btnClick(9)).grid(row=2,column=2)
buttonAdd=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='+',bg='darkslategrey',command=lambda:btnClick('+')).grid(row=2,column=3)

button4=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='4',bg='darkslategrey',command=lambda:btnClick(4)).grid(row=3,column=0)
button5=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='5',bg='darkslategrey',command=lambda:btnClick(5)).grid(row=3,column=1)
button6=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='6',bg='darkslategrey',command=lambda:btnClick(6)).grid(row=3,column=2)
buttonSub=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='-',bg='darkslategrey',command=lambda:btnClick('-')).grid(row=3,column=3)

button1=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='1',bg='darkslategrey',command=lambda:btnClick(1)).grid(row=4,column=0)
button2=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='2',bg='darkslategrey',command=lambda:btnClick(2)).grid(row=4,column=1)
button3=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='3',bg='darkslategrey',command=lambda:btnClick(3)).grid(row=4,column=2)
buttonMulti=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='*',bg='darkslategrey',command=lambda:btnClick('*')).grid(row=4,column=3)

button0=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='0',bg='darkslategrey',command=lambda:btnClick(0)).grid(row=5,column=0)
buttonClear=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='C',bg='darkslategrey',command=btnClear).grid(row=5,column=1)
buttonEqual=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='=',bg='darkslategrey',command=btnEquals).grid(row=5,column=2)
buttonDiv=Button(Calculator_Function,padx=16,pady=1,bd=7,fg='gold',font=('arial',12,'bold'),width=4,text='/',bg='darkslategrey',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()

