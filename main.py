from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os, random
import tempfile
from tkinter import messagebox
from time import strftime
import mysql.connector
import jarvis

class The_Billing_Software:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title(" Developed by Abhikriti Moti and Prabhdeep Singh")

        self.c_name=StringVar()
        self.c_mob=StringVar()
        self.bill_num=StringVar()
        r_num=random.randint(1000,9999)
        self.bill_num.set(r_num)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        self.m=IntVar()
        self.n=IntVar()


        #Categories
        self.Category=["Select Option", "Clothing", "Appliances", "Gadegts"]

        # SubCategories1
        self.SubCatClothing=["Jeans", "T-Shirt","Jackets"]
        self.Jeans=["Killer", "Pepe", "Spykar"]
        self.price_Killer=2999
        self.price_Pepe= 3499
        self.price_Spykar=4999

        self.T_shirt = ["Levis", "Armani", "Van Heusen"]
        self.price_Levis = 2599
        self.price_Armani = 3349
        self.price_VanHeusen = 4499

        self.Jackets = ["Leather", "Denim", "Puffer"]
        self.price_Leather = 8999
        self.price_Denim = 5799
        self.price_Puffer = 6199

        # SubCategories2
        self.SubCatAppliances=["Fridge", "Washing Machines", "Microwave"]
        self.Fridge = ["Haier", "Godrej", "Danby"]
        self.price_Haier = 28999
        self.price_Godrej = 31899
        self.price_Danby = 66000

        self.WashingMachines = ["Bosch", "IFB", "Whirlpool"]
        self.price_Bosch = 24499
        self.price_IFB = 40099
        self.price_Whirlpool = 34900

        self.Microwave = ["Bajaj", "Morphy Richards", "LG"]
        self.price_Bajaj = 10999
        self.price_MorphyRichards = 11599
        self.price_LG = 17699

        # SubCategories3
        self.SubCatGadegts=["Smartphones", "Laptop", "Camera", "Drones", "Accessories"]
        self.Smartphones = ["Samsung", "Sony", "Nokia"]
        self.price_Samsung = 11990
        self.price_Sony = 15999
        self.price_Nokia = 26999

        self.Laptop = ["HP", "Lenovo", "Asus"]
        self.price_HP = 79990
        self.price_Lenovo = 76000
        self.price_Asus = 81999

        self.Camera = ["Canon", "Nikon", "GoPro"]
        self.price_Canon = 71000
        self.price_Nikon = 109000
        self.price_GoPro = 47999

        self.Drones = ["DJI", "Hubsan", "Cheerson"]
        self.price_DJI = 32000
        self.price_Hubsan = 40199
        self.price_Cheerson = 51799

        self.Accessories = ["Charger", "Power Bank", "Tripod"]
        self.price_Charger = 999
        self.price_PowerBank = 1199
        self.price_Tripod = 2199

        # header1
        img1 = Image.open("image/2.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.h_img = ImageTk.PhotoImage(img1)

        lbl_img1=Label(self.root, image=self.h_img)
        lbl_img1.place(x=0, y=0, width=500, height=130)

        # header2
        img2 = Image.open("image/iStock-food delivery.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.h_img2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.h_img2)
        lbl_img2.place(x=500, y=0, width=500, height=130)

        # header3
        img3 = Image.open("image/6.jpg")
        img3 = img3.resize((530, 130), Image.ANTIALIAS)
        self.h_img3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(self.root, image=self.h_img3)
        lbl_img3.place(x=1000, y=0, width=530, height=130)

        # title
        lbl_title1=Label(self.root, text="The Billing Software", font=("times new roman", 30, "bold"),cursor="plus", bg="#EFEFEF", fg="#0033cc")
        lbl_title1.place(x=10, y=130, width=1530, height=45)

        # clock
        def time():
            string = strftime('%a, %H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(lbl_title1, font=('times new roman', 15, 'bold'), background='#EFEFEF', foreground='#0033cc')
        lbl.place(x=2, y=(0), width=170, height=45)
        time()

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE, bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)


        #------------------------------------------------Customer Frame------------------------------------------------
        Cust_Frame=LabelFrame(Main_Frame, text="Customer", font=("times new roman",13,"bold"), bg="#EFEFEF", fg="#0055ff")
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        self.lbl_mob=Label(Cust_Frame,text="Mobile No. ",font=("arial",12,"bold"),bg="#EFEFEF")
        self.lbl_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_mob,font=("times new roman",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        self.lblCustName = Label(Cust_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text ="Customer Name",bd=4)
        self.lblCustName.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame,textvariable=self.c_name, font=("arial", 10, "bold"), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=W,padx=5,pady=2)

        self.lblEmail = Label(Cust_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Email", bd=4)
        self.lblEmail.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame,textvariable=self.c_email, font=("arial", 10, 'bold'), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # -----------------------------------------------Product Frame ------------------------------------------------
        Product_Frame = LabelFrame(Main_Frame, text="Product", font=("times new roman", 13, "bold"), bg="#EFEFEF", fg="#0055ff")
        Product_Frame.place(x=370, y=5, width=620, height=140)

        #Category
        self.lblCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Select Categories", bd=4)
        self.lblCategory.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, value=self.Category, font=("arial", 10, "bold"), width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)

        #SubCategory
        self.lblSubCategory = Label(Product_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Sub Categories", bd=4)
        self.lblSubCategory.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.Combo_SubCategory = ttk.Combobox(Product_Frame, value=[""], font=("arial", 10, "bold"), width=24, state="readonly")
        self.Combo_SubCategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.Combo_SubCategory.bind("<<ComboboxSelected>>",self.Product_add)

        #ProductName
        self.lblproduct = Label(Product_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Product Name", bd=4)
        self.lblproduct.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame, textvariable=self.product, font=("arial", 10, "bold"), width=24, state="readonly")
        self.ComboProduct.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        # Price
        self.lblPrice = Label(Product_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Price", bd=4)
        self.lblPrice.grid(row=0, column=2, stick=W, padx=5, pady=2)

        self.ComboPrice = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=24, state="readonly",textvariable=self.prices)
        self.ComboPrice.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        #Qty
        self.lblQty = Label(Product_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Qty", bd=4)
        self.lblQty.grid(row=1, column=2, stick=W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame, textvariable=self.qty, font=("arial", 10, "bold"), width=26)
        self.ComboQty.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #----------------------------------------------Middle Frame-----------------------------------------------------
        MiddleFrame=Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=150, width=980, height=340)

        btn_add=Button(MiddleFrame, text="Save", command=self.Add_db, cursor="hand2", font=("arial",11,"bold"),width=10, bg="#0055ff", fg="white")
        btn_add.grid(row=0,column=0,padx=28,pady=3)

        btn_upd = Button(MiddleFrame, text="Update", command=self.update_data,cursor="hand2",font=("arial", 11, "bold"), width=10, bg="#0055ff", fg="white")
        btn_upd.grid(row=0, column=1, padx=28, pady=3)

        btn_del = Button(MiddleFrame, text="Delete", command=self.del_data,cursor="hand2", font=("arial", 11, "bold"), width=10, bg="#0055ff", fg="white")
        btn_del.grid(row=0, column=2, padx=28, pady=3)

        #DbFrame
        db_frame=LabelFrame(MiddleFrame,relief=RIDGE,text=" Saved Bills ", font=("times new roman", 13, "bold"),bg="#EFEFEF", fg="#0055ff")
        db_frame.place(x=1,y=40,width=480, height=280)

        # scroll
        scroll_x=ttk.Scrollbar(db_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(db_frame,orient=VERTICAL)

        self.db_table=ttk.Treeview(db_frame,column=("1","2","3","4","5"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.db_table.xview)
        scroll_y.config(command=self.db_table.yview())

        self.db_table.heading("1", text="Bill No.")
        self.db_table.heading("2", text="Phone")
        self.db_table.heading("3", text="Name")
        self.db_table.heading("4", text="Email")
        self.db_table.heading("5", text="Total ₹ ")

        self.db_table["show"]="headings"
        self.db_table.column("1", width=80)
        self.db_table.column("2", width=80)
        self.db_table.column("3", width=80)
        self.db_table.column("4", width=110)
        self.db_table.column("5", width=80)

        self.db_table.pack(fill=BOTH,expand=1)

        self.db_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

        # MiddleImage
        img_b = Image.open("image/4.jpg")
        img_b = img_b.resize((490, 340), Image.ANTIALIAS)
        self.photoimg_b = ImageTk.PhotoImage(img_b)

        lbl_img_b = Label(MiddleFrame, image=self.photoimg_b)
        lbl_img_b.place(x=490,y=0, width=500, height=340)

        #---------------------------------------------Right Frame------------------------------------------------------
        Search_Frame = Frame(Main_Frame, bd=2, bg="#EFEFEF")
        Search_Frame.place(x=1020, y=10, width=470, height=40)

        self.lblBill = Label(Search_Frame, font=("arial", 12, "bold"), fg="#00334d", bg="#EFEFEF", text="Bill No.")
        self.lblBill.grid(row=0, column=0, stick=W, padx=1)

        self.txt_Entry_Search = ttk.Entry(Search_Frame, textvariable=self.search_bill,font=("arial", 10, "bold"), width=26)
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Button(Search_Frame, command=self.find_bill, cursor="hand2", width=10, text="Search", font=("arial", 11, "bold"), bg="#0055ff", fg="white")
        self.BtnSearch.grid(row=0, column=2)

        self.Btn_clearBill = Button(Search_Frame, command=self.NewBill, text="New Bill", bd=2, font=("arial", 11, "bold"), bg="#0055ff", fg="white", width=10, cursor="hand2")
        self.Btn_clearBill.grid(row=0, column=3)

        # Bill Area
        RightLabelFrame = LabelFrame(Main_Frame,text="Bill Area", font=("times new roman", 13, "bold"), bg="#EFEFEF", fg="#0055ff")
        RightLabelFrame.place(x=1000, y=45, width=510, height=440)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame, yscrollcommand=scroll_y.set,bg="white", fg="#00334d", font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #-----------------------------------------Bill Counter --------------------------------------------------------
        Bottom_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=("times new roman", 13, "bold"), bg="#EFEFEF", fg="#0055ff")
        Bottom_Frame.place(x=0, y=485, width=1518, height=125)

        # Sub total
        self.lblSubTotal = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Sub Total", bd=4)
        self.lblSubTotal.grid(row=0, column=0, stick=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(Bottom_Frame, textvariable=self.sub_total, font=("arial", 10, "bold"), width=26)
        self.EntrySubTotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # gst
        self.lbl_tax = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="GST", bd=4)
        self.lbl_tax.grid(row=1, column=0, stick=W, padx=5, pady=2)

        self.txt_tax = ttk.Entry(Bottom_Frame,textvariable=self.tax_input, font=("arial", 10, "bold"), width=26)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # total
        self.lblAmountTotal = Label(Bottom_Frame, font=("arial", 12, "bold"), bg="#EFEFEF", text="Total", bd=4)
        self.lblAmountTotal.grid(row=2, column=0, stick=W, padx=5, pady=2)

        self.txtAmountTotal = ttk.Entry(Bottom_Frame,textvariable=self.total, font=("arial", 10, "bold"), width=26)
        self.txtAmountTotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # ---------------------------------------------Button----------------------------------------------------------
        Btn_Frame=Frame(Bottom_Frame, bd=2, bg="#999999")
        Btn_Frame.place(x=350,y=10)

        self.BtnAddToCart=Button(Btn_Frame, command=self.AddItem, cursor="hand2", width=15, height=2, text="Add To Cart", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnAddToCart.grid(row=0,column=0)

        self.Btngenerate = Button(Btn_Frame, command=self.gen_bill, cursor="hand2", width=12, height=2, text="Generate Bill", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.Btngenerate.grid(row=0, column=1)

        self.BtnSave = Button(Btn_Frame ,command=self.save_bill, cursor="hand2", width=12, height=2, text="Save Bill", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnSave.grid(row=0, column=2)

        self.BtnPrint = Button(Btn_Frame, command=self.iprint, cursor="hand2", width=12, height=2, text="Print", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnPrint.grid(row=0, column=3)

        self.BtnClear = Button(Btn_Frame, command=self.clear, cursor="hand2", width=12, height=2, text="Clear", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnClear.grid(row=0, column=4)

        self.BtnExit = Button(Btn_Frame, command=self.root.destroy, cursor="X_cursor", width=12, height=2, text="Exit", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnExit.grid(row=0, column=5)

        self.BtnInfo = Button(Btn_Frame, command=jarvis.wishMe, cursor="hand2", width=12, height=2, text="Info", font=("arial", 15, "bold"), bg="#0055ff", fg="white")
        self.BtnInfo.grid(row=0, column=6)

        self.welcome()
        self.l=[]

    #-----------------------------------------------Functions Dec-------------------------------------------------------

    def Add_db(self):
        if self.bill_num.get()=="":
            messagebox.showerror('Error', "All Fields Are Required")
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username="root", password="h0ud!n!", database="management")
                mycursor=conn.cursor()
                mycursor.execute("insert into billling values(%s,%s,%s,%s,%s)",(self.bill_num.get(), self.c_mob.get(),self.c_name.get(),self.c_email.get(), self.total.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', "Saved")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")


    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username="root", password="h0ud!n!", database="management")
        mycursor = conn.cursor()
        mycursor.execute('select * from billling')
        data=mycursor.fetchall()
        if len(data)!=0:
            self.db_table.delete(*self.db_table.get_children())
            for i in data:
                self.db_table.insert('',END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.db_table.focus()
        content=self.db_table.item(cursor_row)
        data=content['values']

        self.bill_num.set(data[0])
        self.c_mob.set(data[0])
        self.c_name.set(data[2])
        self.c_email.set(data[3])
        self.total.set(data[4])

    def update_data(self):
        if self.bill_num.get()=="":
            messagebox.showerror('Error', "All Fields Are Required")
        else:
            try:
                update=messagebox.askyesno("Update","Update the DB ?")
                if update>0:
                    conn = mysql.connector.connect(host='localhost', username="root", password="h0ud!n!", database="management")
                    mycursor = conn.cursor()
                    mycursor.execute('update billling set c_mob=%s, c_name=%s, c_email=%s, total=%s where bill_num=%s',(self.c_mob.get(),self.c_name.get(),self.c_email.get(), self.total.get(),self.bill_num.get()))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', "successfully updated")
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}")

    def del_data(self):
        if self.bill_num.get() == "":
            messagebox.showerror('Error', "All Fields Are Required")
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Delete from the DB ?")
                if Delete > 0:
                    conn = mysql.connector.connect(host='localhost', username="root", password="h0ud!n!", database="management")
                    mycursor = conn.cursor()
                    sql='delete from billling where bill_num=%s'
                    value=(self.bill_num.get(),)
                    mycursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', "successfully deleted")
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}")




    def AddItem(self):
        Tax=1
        self.n = self.prices.get()
        self.m = self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error", "Select the Product")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t {self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax) / 100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))

    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error", "Add Items to Cart")
        else:
            text=self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)
            self.textarea.insert(END, "\n=====================================================")
            self.textarea.insert(END, f"\n  Sub Amount:\t\t\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END, f"\n  Tax Amount:\t\t\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END, f"\n  Total Amount:\t\t\t\t\t{self.total.get()}")
            self.textarea.insert(END, "\n=====================================================")

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Save The BILL ?")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('Bills/'+str(self.bill_num.get())+".txt",'w')
            f1.write(self.bill_data)
            op = messagebox.showinfo("Saved Bill", f"Bill Number - {self.bill_num.get()} Saved Successfully ")
            f1.close()

    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")

    def find_bill(self):
        found="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]== self.search_bill.get():
                f1=open(f'Bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found =='no':
            messagebox.showerror("Error", "Bill Not Found")


    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_mob.set("")
        self.c_email.set("")
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()
        self.search_bill.set("")
        x=random.randint(1000, 9999)
        self.bill_num.set(str(x))

    def NewBill(self):
        self.textarea.delete(1.0, END)
        y = random.randint(1000, 9999)
        self.bill_num.set(str(y))
        self.search_bill.set("")
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END, "\t\tWELCOME  TO  THE  SHOP\n")
        self.textarea.insert(END, f"\n INVOICE No. :  {self.bill_num.get()}")
        self.textarea.insert(END, f"\n Customer Name :  {self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:  {self.c_mob.get()}")
        self.textarea.insert(END, f"\n Customer Email :  {self.c_email.get()}")

        self.textarea.insert(END, "\n=====================================================")
        self.textarea.insert(END, f"\n  Products \t\t\tQTY\t\tPrice")
        self.textarea.insert(END, "\n=====================================================\n")

    def Categories(self, event=""):
        if self.Combo_Category.get()=="Clothing":
            self.Combo_SubCategory.config(value=self.SubCatClothing)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Appliances":
            self.Combo_SubCategory.config(value=self.SubCatAppliances)
            self.Combo_SubCategory.current(0)

        if self.Combo_Category.get() == "Gadegts":
            self.Combo_SubCategory.config(value=self.SubCatGadegts)
            self.Combo_SubCategory.current(0)

    def Product_add(self,event=""):
        #"Jeans", "T-Shirt","Jackets"
        if self.Combo_SubCategory.get()=="Jeans":
            self.ComboProduct.config(value=self.Jeans)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "T-Shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Jackets":
            self.ComboProduct.config(value=self.Jackets)
            self.ComboProduct.current(0)

        #"Fridge", "Washing Machines", "Microwave"
        if self.Combo_SubCategory.get()=="Fridge":
            self.ComboProduct.config(value=self.Fridge)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get()=="Washing Machines":
            self.ComboProduct.config(value=self.WashingMachines)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get()=="Microwave":
            self.ComboProduct.config(value=self.Microwave)
            self.ComboProduct.current(0)

        #"Smartphones", "Laptop", "Camera", "Drones", "Accessories"
        if self.Combo_SubCategory.get() == "Smartphones":
            self.ComboProduct.config(value=self.Smartphones)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Laptop":
            self.ComboProduct.config(value=self.Laptop)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Camera":
            self.ComboProduct.config(value=self.Camera)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Drones":
            self.ComboProduct.config(value=self.Drones)
            self.ComboProduct.current(0)

        if self.Combo_SubCategory.get() == "Accessories":
            self.ComboProduct.config(value=self.Accessories)
            self.ComboProduct.current(0)

    def price(self,event=""):
        #Jeans
        if self.ComboProduct.get()=="Killer":
            self.ComboPrice.config(value=self.price_Killer)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Pepe":
            self.ComboPrice.config(value=self.price_Pepe)
            self.ComboPrice.current(0)
            self.qty.set(1)
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_Spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)

        #T_shirt
        if self.ComboProduct.get() == "Levis":
                self.ComboPrice.config(value=self.price_Levis)
                self.ComboPrice.current(0)
                self.qty.set(1)
        if self.ComboProduct.get() == "Armani":
                self.ComboPrice.config(value=self.price_Armani)
                self.ComboPrice.current(0)
                self.qty.set(1)
        if self.ComboProduct.get() == "Van Heusen":
                self.ComboPrice.config(value=self.price_VanHeusen)
                self.ComboPrice.current(0)
                self.qty.set(1)

        #Jackets
        if self.ComboProduct.get() == "Leather":
                    self.ComboPrice.config(value=self.price_Leather)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Denim":
                    self.ComboPrice.config(value=self.price_Denim)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Puffer":
                    self.ComboPrice.config(value=self.price_Puffer)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Fridge
        if self.ComboProduct.get() == "Haier":
                    self.ComboPrice.config(value=self.price_Haier)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Godrej":
                    self.ComboPrice.config(value=self.price_Godrej)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Danby":
                    self.ComboPrice.config(value=self.price_Danby)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #WashingMachines
        if self.ComboProduct.get() == "Bosch":
                    self.ComboPrice.config(value=self.price_Bosch)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "IFB":
                    self.ComboPrice.config(value=self.price_IFB)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Whirlpool":
                    self.ComboPrice.config(value=self.price_Whirlpool)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Microwave
        if self.ComboProduct.get() == "Bajaj":
                    self.ComboPrice.config(value=self.price_Bajaj)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Morphy Richards":
                    self.ComboPrice.config(value=self.price_MorphyRichards)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "LG":
                    self.ComboPrice.config(value=self.price_LG)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Smartphones
        if self.ComboProduct.get() == "Samsung":
                    self.ComboPrice.config(value=self.price_Samsung)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Sony":
                    self.ComboPrice.config(value=self.price_Sony)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Nokia":
                    self.ComboPrice.config(value=self.price_Nokia)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Laptop
        if self.ComboProduct.get() == "HP":
                    self.ComboPrice.config(value=self.price_HP)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Lenovo":
                    self.ComboPrice.config(value=self.price_Lenovo)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Asus":
                    self.ComboPrice.config(value=self.price_Asus)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Camera
        if self.ComboProduct.get() == "Canon":
                    self.ComboPrice.config(value=self.price_Canon)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Nikon":
                    self.ComboPrice.config(value=self.price_Nikon)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "GoPro":
                    self.ComboPrice.config(value=self.price_GoPro)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Drones
        if self.ComboProduct.get() == "DJI":
                    self.ComboPrice.config(value=self.price_DJI)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Hubsan":
                    self.ComboPrice.config(value=self.price_Hubsan)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Cheerson":
                    self.ComboPrice.config(value=self.price_Cheerson)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

        #Accessories
        if self.ComboProduct.get() == "Charger":
                    self.ComboPrice.config(value=self.price_Charger)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Power Bank":
                    self.ComboPrice.config(value=self.price_PowerBank)
                    self.ComboPrice.current(0)
                    self.qty.set(1)
        if self.ComboProduct.get() == "Tripod":
                    self.ComboPrice.config(value=self.price_Tripod)
                    self.ComboPrice.current(0)
                    self.qty.set(1)

if __name__ == '__main__':
    root=Tk()
    obj=The_Billing_Software(root)
    root.mainloop()