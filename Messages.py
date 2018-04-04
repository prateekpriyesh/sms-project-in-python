from tkinter import *
import tkinter.messagebox
import tkinter.ttk
import http.client
class form7:
    def __init__(self):
        self.root8=Tk()
        self.root8.title("ABOUT THIS PROJECT")
        self.lb19=Label(self.root8,fg="purple",font=('arial',15),text="This project is developed by Prateek Priyesh").pack()
        self.lb20=Label(self.root8,fg="purple",font=('arial',15),text="This project is developed with the help of PYTHON language").pack()
        self.lb21=Label(self.root8,fg="purple",font=('arial',15),text="Thankful to VMM Education ").pack()
        self.root8.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------
def view6():
    t=form7()
#---------------------------------------------------------------------------------------------------------------------------
#from here to send the message code start
class form6:
    def send(self):
        mess=self.textbox8.get()
        list4=mess.split(" ")
        ans=""
        for x in list4:
            ans=ans+x+"%20"
        list5=[]
        fileopen2=open("E:\\Project details\\members.txt","r")
        j=0
        while True:
            gpnm=fileopen2.readline()
            if gpnm=="":
                break
            nm=fileopen2.readline()
            ph=fileopen2.readline()
            sp=fileopen2.readline()
            if gpnm==self.cb2.get():
                list5.insert(j,ph)
                j=j+1
        fileopen2.close()
        list5=map(lambda s:s.strip(),list5)
        str1=""
        for z in list5:
            str1=str1+z+","
        conn=http.client.HTTPConnection("server1.vmm.education")
        conn.request('GET',"/VMMCloudMessaging/AWS_SMS_Sender?username=SharmaNayak_py&password=165UCS7J&message="+ans+"&phone_numbers="+str1)
        response=conn.getresponse()
        print(response.read())
        
    def check2(self):
        admin=self.textbox9.get()
        passw=self.textbox10.get()
        if admin=="admin" and passw=="admin":
            self.root7=Tk()
            self.root7.title("Send")
            self.lb18=Label(self.root7,font=('arial',10),text="Enter Group Name").grid(row=0,column=0)
            list2=[]
            fileopen1=open("E:\\Project details\\groups.txt","r")
            i=0
            while True:
                 line3=fileopen1.readline()
                 if line3=="":
                     break
                 line4=fileopen1.readline()
                 line5=fileopen1.readline()
                 list2.insert(i,line3)
                 i=i+1
            fileopen1.close()
            self.cb2=tkinter.ttk.Combobox(self.root7,values=tuple(list2))
            self.cb2.grid(row=0,column=1)
            self.label9=Label(self.root7,font=('arial',10),text="Please enter your message").grid(row=2,column=0)
            self.textbox8=Entry(self.root7,width=60)
            self.textbox8.grid(row=3,column=1)
            self.button18=Button(self.root7,text="Send",command=self.send)
            self.button18.grid(row=4,column=1)
            self.root7.mainloop()
        else:
            tkinter.messagebox.showinfo("Alert!","You are not the administrator of this project")
            
    def __init__(self):
        self.root6=Tk()
        self.root6.title("Administrator Block")
        self.lb11=Label(self.root6,font=('arial',20,'bold'),text="ADMINISTRATOR BLOCK")
        self.lb11.grid(columnspan=4)
        self.lb12=Label(self.root6,text="Administrator")
        self.lb12.grid(row=1,column=0)
        self.textbox9=Entry(self.root6,show="*",width=10)
        self.textbox9.grid(row=1,column=1)
        self.lb13=Label(self.root6,text="Password")
        self.lb13.grid(row=2,column=0)
        self.textbox10=Entry(self.root6,show="*",width=10)
        self.textbox10.grid(row=2,column=1)
        self.bt10=Button(self.root6,padx=12,bd=8,font=('arial',10),text="Login",command=self.check2)
        self.bt10.grid(row=3,column=1)
        
#-------------------------------------------------------------------------------------------------------------------------
def view5():
    k=form6()
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#from here show member coding start
class form5:
    
    def check2(self):
        gpnam1=self.cb2.get()
        number2=self.textbox6.get()
        password=self.widget.get()
        if number2.isnumeric()=="False" or (len(number2))!=10 or password!="123":
            tkinter.messagebox.showinfo("Alert!","You are not registered member confedential details will not be shown")
        else:
            self.root5=Tk()
            self.root5.title("MEMBERS")
            self.root5.geometry("600x600")
            t=tkinter.ttk.Treeview(self.root5,columns=("srno","name","number"))
            t['show']='headings'
            t.heading("srno",text="SR.NO")
            t.heading("name",text="NAME")
            t.heading("number",text="NUMBER")
            rd=open("E:\\Project details\\members.txt","r")
            z=0
            while True:
                  groupname=rd.readline()
                  if groupname=="":
                     break
                  name=rd.readline()
                  number=rd.readline()
                  sep=rd.readline()
                  if groupname==self.cb2.get():
                       t.insert("",z,values=((z+1),name,number))
                       z=z+1
            t.pack()
            self.root5.mainloop()
        
            
        
    def __init__(self):
        self.root4=Tk()
        self.root4.title("VIEW MEMBER")
        self.lb14=Label(self.root4,font=('arial',15,'bold'),text="LOGIN").grid(columnspan=6)
        self.lb7=Label(self.root4,font=('arial',10),text="Enter Group Name").grid(row=1,column=0)
        list2=[]
        fileopen1=open("E:\\Project details\\groups.txt","r")
        i=0
        while True:
            line3=fileopen1.readline()
            if line3=="":
                break
            line4=fileopen1.readline()
            line5=fileopen1.readline()
            list2.insert(i,line3)
            i=i+1
        fileopen1.close()
        self.cb2=tkinter.ttk.Combobox(self.root4,values=tuple(list2))
        self.cb2.grid(row=1,column=1)
        self.lb8=Label(self.root4,font=('arial',10),text="Enter Number").grid(row=2,column=0)
        self.textbox6=Entry(self.root4)
        self.textbox6.grid(row=2,column=1)
        self.lb9=Label(self.root4,font=('arial',10),text="Enter Password").grid(row=3,column=0)
        self.widget=Entry(self.root4,show="*",width=15)
        self.widget.grid(row=3,column=1)
        self.bt10=Button(self.root4,padx=12,bd=8,font=('arial',10),text="Show",command=self.check2)
        self.bt10.grid(row=4,column=1)
        self.root4.mainloop()
#--------------------------------------------------------------------------------------------------------------------------
def view4():
    e=form5()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#from here add member coding start
class form4:
    
    def check1(self):
        gpname=self.cb1.get()
        nm=self.textbox4.get()
        number=self.textbox5.get()
        if gpname=="" or number=="" or nm=="" or (len(number))!=10 or number.isnumeric()=="False":
            tkinter.messagebox.showinfo("Error","All fields are mandotry or please can you check the phone number field")
        else:
            fileopen1=open("E:\\Project details\\members.txt","a")
            fileopen1.write(gpname)
            fileopen1.write(nm)
            fileopen1.write("\n")
            fileopen1.write(number)
            fileopen1.write("\n*************************\n")
            fileopen1.close()
            tkinter.messagebox.showinfo("SUCCESS","Member Added Successfully and as a member to view your group info the login password is 123")
    def __init__(self):
        self.root3=Tk()
        self.root3.title("Add members")
        self.lb15=Label(self.root3,font=('arial',15,'bold'),text="Add Members").grid(columnspan=6)
        self.lb6=Label(self.root3,font=('arial',10),text="Group Name").grid(row=1,column=0)
        list1=[]
        fileopen=open("E:\\Project details\\groups.txt","r")
        i=0
        while True:
            line=fileopen.readline()
            if line=="":
                break
            line1=fileopen.readline()
            line2=fileopen.readline()
            list1.insert(i,line)
            i=i+1
        fileopen.close()
        self.cb1=tkinter.ttk.Combobox(self.root3,values=tuple(list1))
        self.cb1.grid(row=1,column=1)
        self.lb7=Label(self.root3,font=('arial',10),text="Name").grid(row=2,column=0)
        self.textbox4=Entry(self.root3)
        self.textbox4.grid(row=2,column=1)
        self.lb8=Label(self.root3,font=('arial',10),text="Phone Number").grid(row=3,column=0)
        self.textbox5=Entry(self.root3)
        self.textbox5.grid(row=3,column=1)
        self.bt6=Button(self.root3,padx=12,bd=8,font=('arial',10),text="Add",command=self.check1)
        self.bt6.grid(row=4,column=1)
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def view2():
    d=form4()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#from here view group coding start
class form3:
    def __init__(self):
        self.root2=Tk()
        self.root2.title("GROUPS CREATED")
        self.root2.geometry("900x900")
        t=tkinter.ttk.Treeview(self.root2,columns=("group name","description"))
        t['show']='headings'
        t.heading("group name",text="Group Name")
        t.heading("description",text="Description")
        rd=open("E:\\Project details\\groups.txt","r")
        i=0
        while True:
            groupname=rd.readline()
            if groupname=="":
                break
            description=rd.readline()
            sep=rd.readline()
            t.insert("",i,values=(groupname,description))
            i=i+1
        t.pack()
        self.root2.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
def view3():
    c=form3()
#-------------------------------------------------------------------------------------------------------------------------------------------------------
#from here create group coding start
class form2:
    def check(self):
        nm=self.textbox1.get()
        ds=self.textbox2.get()
        if nm=="" or ds=="" :
            tkinter.messagebox.showinfo("OOPS!","ALL FIELDS ARE MANDATORY or you have exceed description limit")
        else:
            obj=open("E:\\Project details\\groups.txt","a")
            name=nm
            des=ds
            obj.write(name)
            obj.write("\n")
            obj.write(des)
            obj.write("\n**********************\n")
            obj.close()
            tkinter.messagebox.showinfo("Thanks!","Your info. has been filled")
    
    def __init__(self):
        self.root1=Tk()
        self.root1.title("Create")
        self.lb3=Label(self.root1,font=('arial',20,'bold'),text="CREATE GROUPS").grid(columnspan=6)
        self.lb4=Label(self.root1,font=('arial',20),text="Group Name").grid(row=1,column=0)
        self.textbox1=Entry(self.root1)
        self.textbox1.grid(row=1,column=1)
        self.lb5=Label(self.root1,font=('arial',20),text="Description").grid(row=2,column=0)
        self.textbox2=Entry(self.root1)
        self.textbox2.grid(row=2,column=1)
        self.bt5=Button(self.root1,padx=12,bd=8,font=('arial',20),text="Submit",command=lambda:self.check()).grid(row=3,column=1)
        self.root1.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------
def view1():
    b=form2()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------
#from here the second screen code start
class form1:
    def __init__(self):
        self.root=Tk()
        self.root.title("MENU")
        self.lb2=Label(self.root,fg='blue',font=('arial',20),text="MESSAGE WORLD").grid(rowspan=6)
        self.bt1=Button(self.root,padx=16,bd=8,font=('arial',20),text="Create Groups",height=4,width=12,command=lambda:view1()).grid(row=0,column=2)
        self.bt2=Button(self.root,padx=16,bd=8,font=('arial',20),text="Add Members",height=4,width=12,command=lambda:view2()).grid(row=0,column=3)
        self.bt3=Button(self.root,padx=16,bd=8,font=('arial',20),text="View Groups",height=4,width=12,command=lambda:view3()).grid(row=1,column=2)
        self.bt4=Button(self.root,padx=16,bd=8,font=('arial',20),text="View Members",height=4,width=12,command=lambda:view4()).grid(row=1,column=3)
        self.bt5=Button(self.root,padx=16,bd=8,font=('arial',20),text="Send Message",height=4,width=12,command=lambda:view5()).grid(row=2,column=2)
        self.bt6=Button(self.root,padx=16,bd=8,font=('arial',20),text="ABOUT",height=4,width=12,command=lambda:view6()).grid(row=2,column=3)
        self.root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def view():
    a=form1()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#from here the main loop start
tk=Tk()
tk.title("Message World")
lb1=Label(tk,fg='blue',font=('Cooper Black',20),text="MESSAGE WORLD").grid(columnspan=6)
bt1=Button(tk,fg='purple',padx=16,bd=8,font=('arial',10,'bold'),text="Start The FUN",command=lambda:view()).grid(row=2,column=3)
tk.mainloop()
