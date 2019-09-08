
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 18:00:35 2019

@author: talha
"""
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
root = Tk()
Inclusive = dict()
Exclusiv = dict()
def main_gui(leaf_nodes_names):
    item = ''
    FeatureNames =  leaf_nodes_names


    def add_inclusive():

        def back():
            combo1.destroy()
            combo.destroy()
            inclusive_submite.destroy()
            inclusive_back.destroy()
            main_gui(FeatureNames)

        def submite_inclusive():
            inc_by = str(combo1.get())
            inc_to = str(combo.get())
            Inclusive[inc_by] = inc_to

        inclusive_add.destroy()
        exclusive.destroy()
        exclusive_add.destroy()
        inclusive_delete.destroy()
        exclusive_delete.destroy()

        combo1=ttk.Combobox(root)
        combo1.grid(row=1,column=1)
        combo1['values'] = FeatureNames
        combo1.current(0)

        inclusive_= Label(root, font=('arial',20,'bold'),text=" To " ,fg = "steel blue",bd=10,anchor='w')
        inclusive_.grid(row=1,column=2)

        combo=ttk.Combobox(root)
        combo.grid(row=1,column=3)
        combo['values'] = FeatureNames
        combo.current(0)

        inclusive_submite= Button(root, command=submite_inclusive, text='Submit')
        inclusive_submite.grid(row= 2, column = 1)

        inclusive_back= Button(root, command=back, text='Back')
        inclusive_back.grid(row= 2, column = 2)

    def delete_inclusive():
        def back1():
            print("back1")
            inclusive_label.destroy()
            combo1.destroy()
            inclusive_.destroy()
            combo.destroy()
            inclusive_submite.destroy()
            inclusive_back.destroy()
            main_gui(FeatureNames)

        def inclusive_delete():
            inc_by = str(combo1.get())

            if len(Inclusive) is not 0:
                if Inclusive[inc_by] is not None:
                    del Inclusive[inc_by]
                else:
                    messagebox.showinfo("Error", inc_by + " not exist in Inclusive")
            else:
                messagebox.showinfo("Error", "No Item in Inclusive")
            # messagebox.destroy()
            delete_inclusive()
        inclusive_label  = Label(root, font=('arial',20,'bold'),text=" Delete Inclusive :" ,fg = "steel blue",bd=10,anchor='w')
        inclusive_label.grid(row=1,column=0)

        combo1=ttk.Combobox(root)
        combo1.grid(row=1,column=1)
        combo1['values'] = FeatureNames
        combo1.current(0)
        try:
            inclusive_add.destroy()
            exclusive.destroy()
            exclusive_add.destroy()
            exclusive_delete.destroy()
        except:
            pass
        inclusive_  = Label(root, font=('arial',20,'bold'),text=" To " ,fg = "steel blue",bd=10,anchor='w')
        inclusive_.grid(row=1,column=2)

        combo=ttk.Combobox(root)
        combo.grid(row=1,column=3)
        combo['values'] = FeatureNames
        combo.current(0)

        inclusive_submite= Button(root, command = inclusive_delete,text='Delete')
        inclusive_submite.grid(row= 2, column = 1)

        inclusive_back= Button(root, command = back1,text='Back')
        inclusive_back.grid(row= 2, column = 2)


    def add_exclusive():
        def back():
            combo1.destroy()
            combo.destroy()
            exclusiv_submite.destroy()
            exclusiv_back.destroy()
            exclusive_label.destroy()
            main_gui(FeatureNames)
        def submite_exclusiv():
            inc_by = str(combo1.get())
            inc_to = str(combo.get())
            Exclusiv[inc_by] = inc_to

        inclusive_add.destroy()
        inclusive.destroy()
        exclusive_add.destroy()
        exclusive_delete.destroy()
        exclusive.destroy()

        combo1=ttk.Combobox(root)
        combo1.grid(row=1,column=1)
        combo1['values'] = FeatureNames
        combo1.current(0)

        exclusive_label  = Label(root, font=('arial',20,'bold'),text=" Delete Exclusive :" ,fg = "steel blue",bd=10,anchor='w')
        exclusive_label.grid(row=1,column=0)
        exclusiv_  = Label(root, font=('arial',20,'bold'),text=" To " ,fg = "steel blue",bd=10,anchor='w')
        exclusiv_.grid(row=1,column=2)

        combo=ttk.Combobox(root)
        combo.grid(row=1,column=3)
        combo['values'] = FeatureNames
        combo.current(0)

        exclusiv_submite= Button(root, command=submite_exclusiv, text='Submite')
        exclusiv_submite.grid(row= 2, column = 1)

        exclusiv_back= Button(root, command=back, text='Back')
        exclusiv_back.grid(row= 2, column = 2)

    def delete_exclusive():

        def back1():

            exclusive_label.destroy()
            combo1.destroy()
            exclusive_.destroy()
            combo.destroy()
            exclusive_submite.destroy()
            exclusive_back.destroy()
            main_gui(FeatureNames)

        def inclusive_delete():

            inc_by = str(combo1.get())
            #inc_to = str(combo.get())
            if len(Exclusiv) is not 0:
                if Exclusiv[inc_by] is not None:
                    del Exclusiv[inc_by]
                else:
                    messagebox.showinfo("Error", inc_by + " not exist in Exclusive")
            else:
                messagebox.showinfo("Error", "No Item in Exclusive")
            messagebox.destroy()
            delete_exclusive()

        exclusive_label  = Label(root, font=('arial',20,'bold'),text=" Delete Exclusive :" ,fg = "steel blue",bd=10,anchor='w')
        exclusive_label.grid(row=1,column=0)

        combo1=ttk.Combobox(root)
        combo1.grid(row=1,column=1)
        combo1['values'] = FeatureNames
        combo1.current(0)
        try:
            inclusive_add.destroy()
            exclusive.destroy()
            exclusive_add.destroy()
            exclusive_delete.destroy()
        except:
            pass
        exclusive_  = Label(root, font=('arial',20,'bold'),text=" To " ,fg = "steel blue",bd=10,anchor='w')
        exclusive_.grid(row=1,column=2)

        combo=ttk.Combobox(root)
        combo.grid(row=1,column=3)
        combo['values'] = FeatureNames
        combo.current(0)

        exclusive_submite= Button(root, command = inclusive_delete,text='Delete')
        exclusive_submite.grid(row= 2, column = 1)

        exclusive_back= Button(root, command = back1,text='Back')
        exclusive_back.grid(row= 2, column = 2)




    name = Label(root, font=('arial',40,'bold'),text="Name" ,fg = "steel blue",bd=10,anchor='w')
    name.grid(row=0,column=0)

    inclusive = Label(root, font=('arial',20,'bold'),text="Inclusive :" ,fg = "steel blue",bd=10,anchor='w')
    inclusive.grid(row=1,column=0)

    inclusive_add= Button(root, command=add_inclusive, text='ADD')
    inclusive_add.grid(row= 1, column = 1)

    inclusive_delete= Button(root, command=delete_inclusive, text='Delete')
    inclusive_delete.grid(row= 1, column = 2)

    exclusive = Label(root, font=('arial',20,'bold'),text="Exclusive :" ,fg = "steel blue",bd=10,anchor='w')
    exclusive.grid(row=2,column=0)

    exclusive_add= Button(root, command=add_exclusive, text='ADD')
    exclusive_add.grid(row= 2, column = 1)

    exclusive_delete= Button(root, command=delete_exclusive, text='Delete')
    exclusive_delete.grid(row= 2, column = 2)


    root.mainloop()
    return {'inclusive':Inclusive,'exclusive':Exclusiv}

