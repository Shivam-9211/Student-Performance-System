# *****=============================================*Student Performance Management System*===================================================******

from tkinter import *
import pandas as pd
import os

win = Tk()
win.title("=====*Student Performance Management System*======")
win.config(bg="blue")

win.grid_columnconfigure(0, weight=1)

def add_std():
    f2=Frame(win,bg="blue")
    f2.grid(padx=100,sticky="ew")

    a1=Label(f2,text="Roll No.")
    b1=Label(f2,text="Student Name")
    c1=Label(f2,text="Father's Name")
    d1=Label(f2,text="Age")
    m12=Label(f2,text="Subjet-1")
    m22=Label(f2,text="Subjet-2")
    m32=Label(f2,text="Subjet-3")
    m42=Label(f2,text="Subjet-4")
    m52=Label(f2,text="Subjet-5")

    a1.grid(row=0,column=0)
    b1.grid(row=0,column=1)
    c1.grid(row=0,column=2)
    d1.grid(row=0,column=3)
    m12.grid(row=0,column=4)
    m22.grid(row=0,column=5)
    m32.grid(row=0,column=6)
    m42.grid(row=0,column=7)
    m52.grid(row=0,column=8)

    a=StringVar()
    b=StringVar()
    c=StringVar()
    d=StringVar()
    m1=StringVar()
    m2=StringVar()
    m3=StringVar()
    m4=StringVar()
    m5=StringVar()
    rollno=Entry(f2,textvariable=a)
    name=Entry(f2,textvariable=b)
    father=Entry(f2,textvariable=c)
    age=Entry(f2,textvariable=d)
    m1entry=Entry(f2,textvariable=m1)
    m2entry=Entry(f2,textvariable=m2)
    m3entry=Entry(f2,textvariable=m3)
    m4entry=Entry(f2,textvariable=m4)
    m5entry=Entry(f2,textvariable=m5)
    rollno.grid(row=1,column=0)
    name.grid(row=1,column=1)
    father.grid(row=1,column=2)
    age.grid(row=1,column=3)
    m1entry.grid(row=1,column=4)
    m2entry.grid(row=1,column=5)
    m3entry.grid(row=1,column=6)
    m4entry.grid(row=1,column=7)
    m5entry.grid(row=1,column=8)

    def submit():

        roll = int(a.get())
        student_name = b.get()
        father_name = c.get()
        age_val = int(d.get())

        sub1 = int(m1.get())
        sub2 = int(m2.get())
        sub3 = int(m3.get())
        sub4 = int(m4.get())
        sub5 = int(m5.get())
        integer = [age_val,sub1, sub2, sub3, sub4, sub5]

        for m in integer:
            if m < 0 or m > 100:
                l2 = Label(f2,text="Marks and Age must be between 0 and 100!")
                l2.grid(row=5,column=4)
                return
        # Load CSV FIRST
        if os.path.exists("Data1.csv"):
            df = pd.read_csv("Data1.csv")
        else:
            df = pd.DataFrame(columns=["Roll_NO.","Student name","Father's name","Age","Sub.1","Sub.2","Sub.3","Sub.4","Sub.5",
                "Total Marks","Percentage","Grade"])

        # Check duplicate roll number
        if roll in df["Roll_NO."].values:
            print("Roll number already exists! Try again.")
            return
                
        total = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = total / 5

        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        elif percentage >= 55:
            grade = "P"
        else:
            grade = "F"

        new_student = {"Roll_NO.": roll,"Student name": student_name,"Father's name": father_name,"Age": age_val,
                    "Sub.1": sub1,"Sub.2": sub2,"Sub.3": sub3,"Sub.4": sub4,"Sub.5": sub5,"Total Marks": total,"Percentage": percentage,"Grade": grade}


        df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
        df = df.sort_values(by="Roll_NO.").reset_index(drop=True)
        df.to_csv("Data1.csv", index=False)
        l=Label(f2,text="Student added Successful")
        l.grid(row=4,column=4)
    
    b7 = Button(f2,text="Submit",font=("Time New Roman",15,"bold"),fg="violet",command=submit)
    b7.grid(row=3,column=4)

def all_std():
    if os.path.exists("Data1.csv"):
        df = pd.read_csv("Data1.csv")
        print("\n--- All Students ---")
        print(df)
        win.destroy()        
    else:
        print("No data found!")

def top5():
    if os.path.exists("Data1.csv"):
        df = pd.read_csv("Data1.csv")
        df = df.sort_values(by="Total Marks", ascending=False)
        print(f"\n--- Top {5} Students ---")
        print(df.head(5))
        win.destroy()
    else:
        print("No data found!")

def low5():
    if os.path.exists("Data1.csv"):
        df = pd.read_csv("Data1.csv")
        df = df.sort_values(by="Total Marks")
        print("\n--- Bottom 5 Students ---")
        print(df.head(5))
        win.destroy()
    else:
        print("No data found!")

def search():
    a=StringVar()
    f3=Frame(win,bg="red")
    f3.grid(padx=100,sticky="ew")
    a1=Label(f3,text="Roll No.")
    a1.grid()
    a1entry=Entry(f3,textvariable=a)
    a1entry.grid()
    def search1():
        if os.path.exists("Data1.csv"):
            df = pd.read_csv("Data1.csv")
            result = df[(df["Roll_NO."] == int(a.get()))]
            if result.empty:
                # print("Student not found!") 
                l=Label(f3,text="Student not found. Try Again!") 
                l.grid()         
            else:
                print("\nStudent Found:")
                print(result)
                win.destroy()       
        else:
            print("No data found!")
    b8 = Button(f3,text="Search",fg="black",command=search1)
    b8.grid()

def delete_std():
    roll_var = StringVar()

    f4 = Frame(win, bg="red")
    f4.grid(padx=100, pady=10, sticky="ew")

    Label(f4, text="Enter Roll No to Delete").grid(row=0, column=0)
    Entry(f4, textvariable=roll_var).grid(row=0, column=1)

    def delete_data():
        if os.path.exists("Data1.csv"):
            df = pd.read_csv("Data1.csv")

            roll = int(roll_var.get())

            if roll in df["Roll_NO."].values:
                df = df[df["Roll_NO."] != roll]   # remove row
                df = df.sort_values(by="Roll_NO.").reset_index(drop=True)
                df.to_csv("Data1.csv", index=False)

                l=Label(f4,text="Student deleted Successful")
                l.grid(row=4,column=2)
            else:
                l=Label(f4,text="Roll No. not found!")
                l.grid(column=2)
        else:
            print("No data found!")

    Button(f4, text="Delete", command=delete_data).grid(row=1, column=1)
    
lab1 = Label(win,text="=====*Student Performance Management System (GUI)*======",font=("Time New Roman",30),bg="red")
lab1.grid(sticky="ew")
f1 = Frame(win,bg="yellow")
f1.grid(ipadx=20,ipady=20, sticky="ew")
# Make frame columns equal
for i in range(7):
    f1.grid_columnconfigure(i, weight=1)

lab2 = Label(f1,text="What You Want to do?-\n" \
"# Add Student- [Press-1]\n# View All Students- [Press-2]\n# Top 5 Students (Highest Marks)- [Press-3]\n" \
"# Bottom 5 Students (Lowest Marks)- [Press-4]\n# Search Student by Roll No.- [Press-5]\n# Delete student by Roll No.- [Press-6]", justify=LEFT, anchor="w",font=("Time New Roman",20),bg="yellow")
lab2.grid(ipadx=30,ipady=20)

b1 = Button(f1,text="1",font=("Time New Roman",30,"bold"),fg="green",border=5,command=add_std)
b1.grid(row=2, column=1)
b2 = Button(f1,text="2",font=("Time New Roman",30,"bold"),fg="green",border=5,command=all_std)
b2.grid(row=2, column=2)
b3 = Button(f1,text="3",font=("Time New Roman",30,"bold"),fg="green",border=5,command=top5)
b3.grid(row=2, column=3)
b4 = Button(f1,text="4",font=("Time New Roman",30,"bold"),fg="green",border=5,command=low5)
b4.grid(row=2, column=4)
b5 = Button(f1,text="5",font=("Time New Roman",30,"bold"),fg="green",border=5,command=search)
b5.grid(row=2, column=5)
b6 =  Button(f1, text="6",font=("Time New Roman",30,"bold"),fg="green",border=5, command=delete_std)
b6.grid(row=2, column=6)
win.mainloop()

# *****===================****========================*****===========================*****================================******