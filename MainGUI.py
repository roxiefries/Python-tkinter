from tkinter import *
from tkinter import messagebox
import backEnd


def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[6])
    entry7.delete(0, END)
    entry7.insert(END, selected_tuple[7])
    entry8.delete(0, END)
    entry8.insert(END, selected_tuple[8])


def view_command():
    listbox.delete(0,END)
    for row in backEnd.view():
        listbox.insert(END, row)


def search_command():
    listbox.delete(0, END)
    for row in backEnd.search(name_text.get(), section_text.get(),student_number_text.get(),
                              midExam_text.get(),midCls_text.get(),finExam_text.get(),finCls_text.get(), finalGrade_text.get()):
        listbox.insert(END, row)


def add_command():
    backEnd.insert(name_text.get(), section_text.get(), student_number_text.get(), midExam_text.get(),midCls_text.get(),
                   finExam_text.get(),finCls_text.get(),finalGrade_text.get())
    listbox.delete(0, END)
    listbox.insert(END,(name_text.get(),section_text.get(), student_number_text.get(), midExam_text.get(),midCls_text.get(),
                        finExam_text.get(),finCls_text.get(), finalGrade_text.get()))


def delete_command():
    backEnd.delete(selected_tuple[0])


def update_command():
    backEnd.update(selected_tuple[0],name_text.get(),section_text.get(), student_number_text.get(),
                   midExam_text.get(),midCls_text.get(),finExam_text.get(),finCls_text.get(), finalGrade_text.get())


def clear_command():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)


#####################################################
def calculator():
    def check():
        rec=main.get()
        tt=total.get()
        if rec<0:
            return messagebox.showerror('Error','Invalid')
        elif rec==0:
            return messagebox.showerror('Error','Invalid')
        elif tt<0:
            return messagebox.showerror('Error','Invalid')
        elif tt==0:
            return messagebox.showerror('Error','Invalid')
        else:
            result=(rec/tt)*100
            last=round(result)
            messagebox.showinfo('Result',str(last)+'%')
    calc=Toplevel()
    main=IntVar()
    total=IntVar()
    calc.geometry('400x400')
    calc.title('percentage calculator')

    Label(calc,text='ENTER MARK, ',font='Helvetica 12 bold').grid(row=1,column=4)
    Label(calc,text='marks').grid(row=2,column=2)
    Entry(calc,width=3,textvariable=main).grid(row=3,column=2)
    Label(calc,text='/').grid(row=2,column=3)
    Label(calc,text='Total').grid(row=2,column=4)
    Entry(calc,width=3,textvariable=total).grid(row=3,column=4)
    Button(calc,text='Calculate',command=check).grid(row=4,column=5)

#####################################################
mainWindow = Tk()
mainWindow.title("Class Room Management Application")

label1=Label(mainWindow, text="Student Records ", font='Helvetica 12 bold')
label1.grid(row=0, column=0)
label2=Label(mainWindow, text="Student Name :")
label2.grid(row=1, column=0)
label3=Label(mainWindow, text="Student Section :")
label3.grid(row=2, column=0)
label4=Label(mainWindow, text="Student Id :")
label4.grid(row=3, column=0)
label5=Label(mainWindow, text="Midterm Exam :")
label5.grid(row=4, column=0)
label6=Label(mainWindow, text="Midterm Class Standing :")
label6.grid(row=5, column=0)
label7=Label(mainWindow, text="Final Exam :")
label7.grid(row=6, column=0)
label8=Label(mainWindow, text="Final Class Standing :")
label8.grid(row=7, column=0)
label9=Label(mainWindow, text="FINAL GRADE :")
label9.grid(row=8, column=0)

name_text=StringVar()
entry1=Entry(mainWindow, textvariable=name_text)
entry1.grid(row=1, column=1)

section_text=StringVar()
entry2=Entry(mainWindow, textvariable=section_text)
entry2.grid(row=2, column=1)

student_number_text=StringVar()
entry3=Entry(mainWindow, textvariable=student_number_text)
entry3.grid(row=3, column=1)

midExam_text=StringVar()
entry4=Entry(mainWindow, textvariable=midExam_text)
entry4.grid(row=4, column=1)

midCls_text=StringVar()
entry5=Entry(mainWindow, textvariable=midCls_text)
entry5.grid(row=5, column=1)

finExam_text=StringVar()
entry6=Entry(mainWindow, textvariable=finExam_text)
entry6.grid(row=6, column=1)

finCls_text=StringVar()
entry7=Entry(mainWindow, textvariable=finCls_text)
entry7.grid(row=7, column=1)

finalGrade_text=StringVar()
entry8=Entry(mainWindow, textvariable=finalGrade_text)
entry8.grid(row=8, column=1)

listbox = Listbox(mainWindow, height=30 , width=70)
listbox.grid(row=1, column = 3, rowspan=8, columnspan = 2)

scrollBar = Scrollbar(mainWindow)
scrollBar.grid(row=1,column=2, sticky='ns', rowspan=8)

listbox.configure(yscrollcommand=scrollBar.set)
scrollBar.configure(command=listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(mainWindow,text="view records",width=12, command=view_command,bg='yellow')
b1.grid(row=9, column=0)

b2=Button(mainWindow,text="add student",width=12, command= add_command, bg='yellow')
b2.grid(row=10, column=0)

b3=Button(mainWindow,text="delete record",width=12, command= delete_command, bg='yellow')
b3.grid(row=9, column=1)

b4=Button(mainWindow,text="search student",width=12, command=search_command, bg='yellow')
b4.grid(row=10, column=1)

b5=Button(mainWindow,text="update record",width=12, command=update_command, bg='yellow')
b5.grid(row=9, column=2)

b6=Button(mainWindow,text="clear all",width=12, command=clear_command, bg='yellow')
b6.grid(row=10, column=2)

b7=Button(mainWindow,text="calculate percentage",width=15, command=calculator, bg='yellow')
b7.grid(row=9, column=3)

b8=Button(mainWindow,text="exit application",width=15, command=mainWindow.destroy, bg='yellow')
b8.grid(row=10, column=3)
mainWindow.mainloop()
