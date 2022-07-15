from tkinter import*
from PIL import Image,ImageTk #install pillow
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventry management system | developed by sanket")
        self.root.config(bg="white")

        #====title=====
        self.icon_title=PhotoImage(file="images/logo1.png")

        title=Label(self.root,text="Inventry Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===btn_logout===
        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #====clock bar===
        self.lbl_clock=Label(self.root,text="Welcome to inventry mangement system \t\t Date:DD_MM_YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left menu===== 
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        #=======left side frame define
        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
        #=====left side menu image design with resize function==

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        #=====left side menu label design===
        self.icon_side=PhotoImage(file="images/side.png")
        
        lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman" ,20),bg="#009688").pack()
        
        #===left menu button====
        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)   
        
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)    

        #===content===
        self.lbl_employee=Label(self.root,text="Total Employee\n[0]",bg="#33bbf9",relief=RIDGE,fg="white",font=("goudy old style",20, "bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="Total supplier\n[0]",bg="#ff5722",relief=RIDGE,fg="white",font=("goudy old style",20, "bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_categery=Label(self.root,text="Total categary\n[0]",bg="#009688",relief=RIDGE,fg="white",font=("goudy old style",20, "bold"))
        self.lbl_categery.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="Total Product\n[0]",bg="#607d8b",relief=RIDGE,fg="white",font=("goudy old style",20, "bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[0]",bg="#ffc107",relief=RIDGE,fg="white",font=("goudy old style",20, "bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)        


        #====footter=====
        lbl_footer=Label(self.root,text="IMS- Inventry Management System | Developed by Sanket\n For any technical issue contact : 8669xxxx96",font=("times new roman",12),bg="#4d636d",bd=5,fg="white").pack(side=BOTTOM,fill=X)

        #============














#==========================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
#==========================================================
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
#==========================================================
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
#==========================================================
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
#==========================================================
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)





if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()