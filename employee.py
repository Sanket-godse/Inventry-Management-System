from tkinter import*
from tkinter import font
from PIL import Image,ImageTk #install pillow
from tkinter import ttk,messagebox
import sqlite3


class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventry management system | developed by sanket")
        self.root.config(bg="white")
        self.root.focus_force()
        #==================================================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()


        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        


        #======search frame===============================
        SearchFrame=LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2)
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #=====option=======================================
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,value=("select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)
        #======search entry================================
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        #==========search button==========================
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #=========title==================================
        title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        #======Content========================
        #=========row -1=================
        lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)

        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)

        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)

        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)

        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,value=("select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)        

        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)

        #==============row-2=========================
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)

        lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)

        lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)

        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)     

        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #==============row-3=========================
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)

        lbl_pass=Label(self.root,text="Passward",font=("goudy old style",15),bg="white").place(x=350,y=230)

        lbl_utype=Label(self.root,text="User type",font=("goudy old style",15),bg="white").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)

        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)     

        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,value=("Admin","Employee",),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #==============row-4=========================
        lbl_address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)

        lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)

        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)

        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)     

        #======button ==================================
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)

        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)

        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)

        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)

        #==============Employee details===================
        #==============frame design======================
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        #==============scroll bar=======================
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployTable.xview)
        scrolly.config(command=self.EmployTable.yview)

        self.EmployTable.heading("eid",text="EMP ID")
        self.EmployTable.heading("name",text="NAME")
        self.EmployTable.heading("email",text="Email")
        self.EmployTable.heading("gender",text="Gender")
        self.EmployTable.heading("contact",text="Contact")
        self.EmployTable.heading("dob",text="DOB")
        self.EmployTable.heading("doj",text="DOJ")
        self.EmployTable.heading("pass",text="Passward")
        self.EmployTable.heading("utype",text="User type")
        self.EmployTable.heading("address",text="Address")
        self.EmployTable.heading("salary",text="Sallary")

        self.EmployTable["show"]="headings"

        self.EmployTable.column("eid",width=90)
        self.EmployTable.column("name",width=90)
        self.EmployTable.column("email",width=90)
        self.EmployTable.column("gender",width=90)
        self.EmployTable.column("contact",width=90)
        self.EmployTable.column("dob",width=90)
        self.EmployTable.column("doj",width=90)
        self.EmployTable.column("pass",width=90)
        self.EmployTable.column("utype",width=90)
        self.EmployTable.column("address",width=90)
        self.EmployTable.column("salary",width=90)
        self.EmployTable.pack(fill=BOTH,expand=1)
        self.EmployTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()      




#=========================================================
#==================datebase work========================

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        #============validation for employee id==========
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)   
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee ID alredy assigned ,try diffrent",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                self.var_emp_id.get(),
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_address.get(1.0,END),
                                self.var_salary.get()
                    ))  
                    con.commit()
                    messagebox.showinfo("Success","Employee added Successfully",parent=self.root)  
                    self.show()        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    #======================================================
    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()                                
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployTable.delete(*self.EmployTable.get_children())
            for row in rows:
                self.EmployTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 

    #==================================================
    def get_data(self,ev):
        f=self.EmployTable.focus()
        content=(self.EmployTable.item(f))
        row=content['values']

        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]),
        self.txt_address.delete(1.0,END),
        self.txt_address.insert(END,row[9]),
        self.var_salary.set(row[10]),
    #====================================================
    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        #============validation for employee id==========
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)   
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    cur.execute("update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                self.var_name.get(),
                                self.var_email.get(),
                                self.var_gender.get(),
                                self.var_contact.get(),
                                self.var_dob.get(),
                                self.var_doj.get(),
                                self.var_pass.get(),
                                self.var_utype.get(),
                                self.txt_address.get(1.0,END),
                                self.var_salary.get(),
                                self.var_emp_id.get()
                    ))  
                    con.commit()
                    messagebox.showinfo("Success","Employee updated Successfully",parent=self.root)  
                    self.show()        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                    
    #=====================================================
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        #============validation for employee id==========
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)   
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm ","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showerror("Delete","Employee deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"),
        self.txt_address.delete('1.0',END),
        self.var_salary.set(""),
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    def search(self): 

        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()                                
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search area should be required ",parent=self.root)
            else:

                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployTable.delete(*self.EmployTable.get_children())
                    for row in rows:
                        self.EmployTable.insert('',END,values=row)
                else:
                    messagebox.showerror("error","No record found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root) 


if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()