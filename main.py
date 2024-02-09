from tkinter import *
import random
import os
from tkinter import messagebox
import mysql.connector as msql
from datetime import datetime

connection = msql.connect(host="localhost", user="root", password="Vinit2004@", database="Billing_system")

cursor = connection.cursor()


# main
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("VU STORES")
        bg_color = "#E8E4D6"
        title = Label(self.root, text="VU STORES", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg=bg_color,
                      fg="Black", relief=GROOVE)
        title.pack(fill=X)
        # medical
        self.sanitizer = IntVar()
        self.mask = IntVar()
        self.hand_gloves = IntVar()
        self.dettol = IntVar()
        self.newsprin = IntVar()
        self.thermal_gun = IntVar()
        # grocery
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        # cold drink
        self.sprite = IntVar()
        self.limca = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_dew = IntVar()
        # total product price
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
        # Customer
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.search_bill = StringVar()
        # Tax
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
        # setup price
        cursor.execute("SELECT rate FROM Price Where Item = 'Sanitizer'")
        self.sanitizer_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Mask'")
        self.mask_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Hand Gloves'")
        self.handgloves_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Dettol'")
        self.dettol_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Newsprin'")
        self.newsprin_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Thermal Gun'")
        self.thermalgun_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Rice'")
        self.rice_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Food Oil'")
        self.foodoil_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Wheat'")
        self.wheat_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Dal'")
        self.dal_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Flour'")
        self.flour_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Maggie'")
        self.maggie_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Sprite'")
        self.sprite_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Limca'")
        self.limca_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Mazza'")
        self.mazza_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Coke'")
        self.coke_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Fanta'")
        self.fanta_price = cursor.fetchone()[0]
        cursor.execute("SELECT rate FROM Price Where Item = 'Mountain Dew'")
        self.mountaindew_price = cursor.fetchone()[0]
        # customer retail details
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", fg="Black", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", fg="Black", bg=bg_color, font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", fg="Black", bg=bg_color, font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=15, height=1, font=('arial', 15, 'bold'),
                         relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

        # Medical
        F2 = LabelFrame(self.root, text="Medical Purpose", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F2.place(x=5, y=180, width=325, height=380)

        sanitizer_lbl = Label(F2, text="Sanitizer", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        sanitizer_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sanitizer_txt = Entry(F2, width=10, textvariable=self.sanitizer, font=('times new roman', 16, 'bold'), bd=5,
                              relief=GROOVE)
        sanitizer_txt.grid(row=0, column=1, padx=10, pady=10)

        mask_lbl = Label(F2, text="Mask", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mask_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        mask_txt = Entry(F2, width=10, textvariable=self.mask, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        mask_txt.grid(row=1, column=1, padx=10, pady=10)

        hand_gloves_lbl = Label(F2, text="Hand Gloves", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        hand_gloves_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        hand_gloves_txt = Entry(F2, width=10, textvariable=self.hand_gloves, font=('times new roman', 16, 'bold'), bd=5,
                                relief=GROOVE)
        hand_gloves_txt.grid(row=2, column=1, padx=10, pady=10)

        dettol_lbl = Label(F2, text="Dettol", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        dettol_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        dettol_txt = Entry(F2, width=10, textvariable=self.dettol, font=('times new roman', 16, 'bold'), bd=5,
                           relief=GROOVE)
        dettol_txt.grid(row=3, column=1, padx=10, pady=10)

        newsprin_lbl = Label(F2, text="Newsprin", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        newsprin_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        newsprin_txt = Entry(F2, width=10, textvariable=self.newsprin, font=('times new roman', 16, 'bold'), bd=5,
                             relief=GROOVE)
        newsprin_txt.grid(row=4, column=1, padx=10, pady=10)

        thermal_gun_lbl = Label(F2, text="Thermal Gun", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        thermal_gun_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        thermal_gun_txt = Entry(F2, width=10, textvariable=self.thermal_gun, font=('times new roman', 16, 'bold'), bd=5,
                                relief=GROOVE)
        thermal_gun_txt.grid(row=5, column=1, padx=10, pady=10)

        # Grocery Items
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F3.place(x=340, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5,
                             relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

        # Cold Drink
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5,
                           relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        limca_lbl = Label(F4, text="Limca", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        limca_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        limca_txt = Entry(F4, width=10, textvariable=self.limca, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        limca_txt.grid(row=1, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mazza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F4, width=10, textvariable=self.mazza, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5,
                         relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5,
                          relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_dew_lbl = Label(F4, text="Mountain Dew", font=('times new roman', 16, 'bold'), bg=bg_color, fg="black")
        mountain_dew_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_duo_txt = Entry(F4, width=10, textvariable=self.mountain_dew, font=('times new roman', 16, 'bold'),
                                 bd=5, relief=GROOVE)
        mountain_duo_txt.grid(row=5, column=1, padx=10, pady=10)

        # Bill Area
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, bg='White', fg='Black', yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Buttoon Frame
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="Black",
                        bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Medical Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m1_lbl.grid(row=0, column=0, padx=20, pady=1, sticky='W')
        m1_txt = Entry(F6, width=18, textvariable=self.medical_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m1_txt.grid(row=0, column=1, padx=18, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg=bg_color,
                       fg="black")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m4_lbl = Label(F6, text="Medical Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m4_lbl.grid(row=0, column=2, padx=20, pady=1, sticky='W')
        m4_txt = Entry(F6, width=18, textvariable=self.medical_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m4_txt.grid(row=0, column=3, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg=bg_color, fg="black")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

        # Buttons
        btn_f = Frame(F6, bd=7, bg='dark grey', relief=GROOVE)
        btn_f.place(x=760, width=565, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="Black", bd=2, fg="black", pady=15, width=10,
                           font='arial 15 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=5)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="black",
                                  pady=15, width=10, font='arial 15 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="Black", bd=2, fg="black", pady=15,
                           width=10, font='arial 15 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="Black", fg="black", pady=15, width=10,
                          font='arial 15 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    # total bill
    def total(self):
        self.m_h_g_p = self.hand_gloves.get()
        self.m_s_p = self.sanitizer.get() * self.sanitizer_price
        self.m_m_p = self.mask.get() * self.mask_price
        self.m_d_p = self.dettol.get() * self.dettol_price
        self.m_n_p = self.newsprin.get() * self.newsprin_price
        self.m_t_g_p = self.thermal_gun.get() * self.thermalgun_price
        self.total_medical_price = float(
            self.m_m_p + self.m_h_g_p + self.m_d_p + self.m_n_p + self.m_t_g_p + self.m_s_p)

        self.medical_price.set("Rs. " + str(self.total_medical_price))
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax.set("Rs. " + str(self.c_tax))

        self.g_r_p = self.rice.get() * self.rice_price
        self.g_f_o_p = self.food_oil.get() * self.foodoil_price
        self.g_w_p = self.wheat.get() * self.wheat_price
        self.g_d_p = self.daal.get() * self.dal_price
        self.g_f_p = self.flour.get() * self.flour_price
        self.g_m_p = self.maggi.get() * self.maggie_price
        self.total_grocery_price = float(self.g_r_p + self.g_f_o_p + self.g_w_p + self.g_d_p + self.g_f_p + self.g_m_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get() * self.sprite_price
        self.c_d_l_p = self.limca.get() * self.limca_price
        self.c_d_m_p = self.mazza.get() * self.mazza_price
        self.c_d_c_p = self.coke.get() * self.coke_price
        self.c_d_f_p = self.fanta.get() * self.fanta_price
        self.c_m_d = self.mountain_dew.get() * self.mountaindew_price
        self.total_cold_drinks_price = float(
            self.c_d_s_p + self.c_d_l_p + self.c_d_m_p + self.c_d_c_p + self.c_d_f_p + self.c_m_d)

        self.cold_drinks_price.set("Rs. " + str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. " + str(self.c_d_tax))

        self.total_bill = float(
            self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

    # welcome bill

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWELCOME TO SVKM KIRANA")
        cursor.execute("SELECT MAX(Bill_no) FROM Bill")
        x = cursor.fetchone()[0] + 1
        self.bill_no.set(str(x))
        self.txtarea.insert(END, f"\nBill Number:{self.bill_no.get()}\t\t\t Date: {datetime.now().date()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number:{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

    # Bill Area
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get() == "Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
        # Medical
        if self.sanitizer.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.sanitizer.get()}\t\t{self.m_s_p}")
        if self.mask.get() != 0:
            self.txtarea.insert(END, f"\n Mask\t\t{self.mask.get()}\t\t{self.m_m_p}")
        if self.hand_gloves.get() != 0:
            self.txtarea.insert(END, f"\n Hand Gloves\t\t{self.hand_gloves.get()}\t\t{self.m_h_g_p}")
        if self.dettol.get() != 0:
            self.txtarea.insert(END, f"\n Dettol\t\t{self.dettol.get()}\t\t{self.m_d_p}")
        if self.newsprin.get() != 0:
            self.txtarea.insert(END, f"\n Newsprin\t\t{self.newsprin.get()}\t\t{self.m_n_p}")
        if self.thermal_gun.get() != 0:
            self.txtarea.insert(END, f"\n Thermal Gun\t\t{self.sanitizer.get()}\t\t{self.m_t_g_p}")
        # Grocery
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        # Cold Drink
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.limca.get() != 0:
            self.txtarea.insert(END, f"\n Limca\t\t{self.limca.get()}\t\t{self.c_d_l_p}")
        if self.mazza.get() != 0:
            self.txtarea.insert(END, f"\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Coke\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta\t\t{self.fanta.get()}\t\t{self.c_d_f_p}")
        if self.mountain_dew.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Dew\t\t{self.rmountain_dew.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # Taxes
        if self.medical_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Medical Tax\t\t\t{self.medical_tax.get()}")
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    # Save Bill
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/" + str(self.c_name.get()) + "_" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            print(self.bill_no.get(), self.total_bill)
            a = int(self.bill_no.get())
            b = self.total_bill

            sql = "INSERT INTO Bill (Bill_no, Total_bill, Date) VALUES (%s, %s, %s)"

            cursor.execute(sql, (a, b, datetime.now().date()))
            # data_to_insert = (int(self.bill_no.get()), self.total_bill)
            # cursor.execute(insert_query)
            connection.commit()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
            return

    # Find Bill
    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):

            if i.split('.')[0] == self.search_bill.get():

                with open(f"bills/{i}", "r") as file:
                    var = file.read()
                    self.txtarea.delete("1.0", END)
                    for d in var:
                        self.txtarea.insert(END, d)
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # Clear Bill
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
            self.sanitizer.set(0)
            self.mask.set(0)
            self.hand_gloves.set(0)
            self.dettol.set(0)
            self.newsprin.set(0)
            self.thermal_gun.set(0)
            # Grocery
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
            # Cold drink
            self.sprite.set(0)
            self.limca.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_dew.set(0)
            # Taxes
            self.medical_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.medical_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.search_bill.set("")

            self.welcome_bill()

    # Exit
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            cursor.close()
            connection.close()
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
